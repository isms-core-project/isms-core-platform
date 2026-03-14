#!/usr/bin/env bash
# ============================================================================
# ISMS CORE Platform — First Boot Bootstrap
#
# Run this ONCE after the stack is up for the first time (fresh volumes).
# It stamps Alembic, runs all migrations, then imports all content into the DB.
#
# Usage:
#   chmod +x bootstrap.sh
#   ./bootstrap.sh
# ============================================================================

set -euo pipefail

API=https://localhost

# ---- Colours ---------------------------------------------------------------
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'
ok()   { echo -e "${GREEN}  ✓ $*${NC}"; }
info() { echo -e "${YELLOW}  → $*${NC}"; }
fail() { echo -e "${RED}  ✗ $*${NC}"; exit 1; }

echo "============================================================================"
echo " ISMS CORE Platform — First Boot Bootstrap"
echo "============================================================================"

# ---- Wait for backend health -----------------------------------------------
info "Waiting for backend to be healthy..."
for i in $(seq 1 60); do
    if curl -sfk "$API/health" > /dev/null 2>&1; then
        ok "Backend healthy"
        break
    fi
    if [ $i -eq 60 ]; then
        fail "Stack did not become healthy after 120s — check: docker compose logs isms-core-nginx isms-core-backend"
    fi
    sleep 2
done

# Migrations run automatically via backend entrypoint.sh on startup.
# ---- Auth token ------------------------------------------------------------
BOOTSTRAP_EMAIL="${ADMIN_EMAIL:-admin@isms-core.dev}"
BOOTSTRAP_PASSWORD="${ADMIN_PASSWORD:-admin123}"

info "Getting admin token (${BOOTSTRAP_EMAIL})..."
RESPONSE=$(curl -sfk -X POST "$API/api/v1/auth/login" \
    -H 'Content-Type: application/json' \
    -d "{\"email\":\"${BOOTSTRAP_EMAIL}\",\"password\":\"${BOOTSTRAP_PASSWORD}\"}") || \
    fail "Login failed — check backend logs"
TOKEN=$(echo "$RESPONSE" | python3 -c 'import sys,json; print(json.load(sys.stdin)["access_token"])')
ok "Authenticated as admin@isms-core.dev"

# Helper: POST an admin endpoint and show result
run_import() {
    local label="$1"
    local endpoint="$2"
    info "$label..."
    RESULT=$(curl -sfk -X POST "$API/api/v1/admin/$endpoint" \
        -H "Authorization: Bearer $TOKEN") || \
        fail "$label failed — check backend logs"
    echo "$RESULT" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    s = d.get('stats', d)
    parts = []
    for k, v in s.items():
        if isinstance(v, int) and 'error_detail' not in k:
            parts.append(f'{k}={v}')
    print('    ' + ', '.join(parts[:6]))
except: pass
"
    ok "$label complete"
}

# ---- Import sequence -------------------------------------------------------
echo ""
echo "--- Importing content ---"

run_import "Step 1/6: Loading framework datasets" "load"
run_import "Step 2/6: Importing policies (FW + OP + PRIV + CLD)" "import-policies"
run_import "Step 3/6: Importing implementations (IMP-UG/TG)" "import-implementations"
run_import "Step 4/6: Importing operational checklists" "import-operational"
run_import "Step 5/6: Importing privacy/cloud checklists" "import-privacy"
run_import "Step 6/6: Importing framework workbook structure" "import-framework-workbooks"

info "Reindexing OpenSearch..."
curl -sfk -X POST "$API/api/v1/admin/reindex" \
    -H "Authorization: Bearer $TOKEN" > /dev/null
ok "OpenSearch reindex complete"

# ---- Summary ---------------------------------------------------------------
echo ""
echo "============================================================================"
ok "Bootstrap complete!"
echo ""
OVERVIEW=$(curl -sfk "$API/api/v1/dashboard/overview" \
    -H "Authorization: Bearer $TOKEN" 2>/dev/null || echo '{}')
echo "$OVERVIEW" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    fw = d.get('framework', {})
    print(f\"  Controls:        {d.get('total_controls', '?')}\")
    print(f\"  Policies:        {d.get('total_policies', '?')}\")
    print(f\"  Implementations: {d.get('total_implementations', '?')}\")
    print(f\"  Assessments:     {d.get('total_assessments', '?')}\")
    print(f\"  FW coverage:     {fw.get('coverage_pct', '?')}%\")
except: pass
" 2>/dev/null || true

echo ""
HOST="${HOST_IP:-$(hostname -I | awk '{print $1}')}"
echo "  Platform:  https://${HOST}  (accept self-signed cert or use FQDN)"
echo "  API docs:  https://${HOST}/api/docs"
echo "  Login:     ${BOOTSTRAP_EMAIL} / ${BOOTSTRAP_PASSWORD}"
echo ""
echo "  Email:     docker compose --profile mailpit up -d  (then http://${HOST}:8025)"
echo "  TLS/FQDN:  ./nginx/scripts/setup-letsencrypt.sh <domain> <email>"
echo "============================================================================"
