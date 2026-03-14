#!/usr/bin/env bash
# ============================================================================
# ISMS CORE — Let's Encrypt certificate setup
#
# Requires:
#   - certbot installed on the host (apt install certbot)
#   - Port 80 publicly reachable from the internet
#   - FQDN pointing to this server's public IP
#
# Usage:
#   chmod +x nginx/scripts/setup-letsencrypt.sh
#   ./nginx/scripts/setup-letsencrypt.sh yourdomain.com admin@yourdomain.com
#
# After running: set FQDN=yourdomain.com in .env and restart nginx:
#   docker compose restart isms-core-nginx
# ============================================================================

set -euo pipefail

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'
ok()   { echo -e "${GREEN}  ✓ $*${NC}"; }
info() { echo -e "${YELLOW}  → $*${NC}"; }
fail() { echo -e "${RED}  ✗ $*${NC}"; exit 1; }

DOMAIN="${1:-}"
EMAIL="${2:-}"

[ -z "$DOMAIN" ] && fail "Usage: $0 <domain> <email>"
[ -z "$EMAIL"  ] && fail "Usage: $0 <domain> <email>"

command -v certbot >/dev/null 2>&1 || fail "certbot not found. Install with: apt install certbot"

echo "========================================================================"
echo " ISMS CORE — Let's Encrypt certificate setup"
echo " Domain: $DOMAIN   Email: $EMAIL"
echo "========================================================================"

# Temporarily stop nginx so certbot can use port 80
info "Stopping isms-core-nginx for ACME challenge..."
docker compose stop isms-core-nginx 2>/dev/null || true

info "Requesting certificate from Let's Encrypt..."
certbot certonly \
    --standalone \
    --non-interactive \
    --agree-tos \
    --email "$EMAIL" \
    -d "$DOMAIN"
ok "Certificate issued: /etc/letsencrypt/live/$DOMAIN/"

info "Updating .env with FQDN=$DOMAIN ..."
if grep -q "^FQDN=" .env 2>/dev/null; then
    sed -i "s|^FQDN=.*|FQDN=$DOMAIN|" .env
else
    echo "FQDN=$DOMAIN" >> .env
fi
ok ".env updated"

info "Restarting nginx..."
docker compose up -d isms-core-nginx
ok "nginx restarted with Let's Encrypt certificate"

echo ""
echo "========================================================================"
ok "TLS setup complete!"
echo "  Platform: https://$DOMAIN"
echo ""
echo "  Auto-renewal: add to crontab:"
echo "  0 3 * * * certbot renew --quiet && docker compose restart isms-core-nginx"
echo "========================================================================"
