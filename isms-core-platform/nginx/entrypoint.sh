#!/bin/sh
# ============================================================================
# ISMS CORE — nginx TLS entrypoint
#
# Certificate resolution order (first match wins):
#   1. Let's Encrypt  — /etc/letsencrypt/live/$FQDN/ exists (certbot ran)
#   2. Custom cert    — /etc/nginx/certs/cert.pem + key.pem placed by operator
#   3. Self-signed    — auto-generated on first boot (default, works anywhere)
#
# Env vars:
#   NGINX_HOST   IP or FQDN used in self-signed SAN + nginx server_name (required)
#   FQDN         Domain for Let's Encrypt (optional — only needed for mode 1)
# ============================================================================
set -e

CERT_DIR=/etc/nginx/certs
LE_LIVE=/etc/letsencrypt/live

mkdir -p "$CERT_DIR"

# ── Mode 1: Let's Encrypt ────────────────────────────────────────────────────
if [ -n "$FQDN" ] && [ -f "$LE_LIVE/$FQDN/fullchain.pem" ]; then
    echo "[nginx/tls] Mode: Let's Encrypt ($FQDN)"
    ln -sf "$LE_LIVE/$FQDN/fullchain.pem" "$CERT_DIR/cert.pem"
    ln -sf "$LE_LIVE/$FQDN/privkey.pem"   "$CERT_DIR/key.pem"

# ── Mode 2: Custom cert (local CA or purchased) ──────────────────────────────
elif [ -f "$CERT_DIR/cert.pem" ] && [ -f "$CERT_DIR/key.pem" ]; then
    echo "[nginx/tls] Mode: Custom certificate ($CERT_DIR/cert.pem)"

# ── Mode 3: Self-signed (auto-generate) ─────────────────────────────────────
else
    echo "[nginx/tls] Mode: Self-signed (no certificate found — generating...)"
    HOST="${NGINX_HOST:-localhost}"
    # Build SAN: add both IP and DNS entries so browsers accept it
    if echo "$HOST" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'; then
        SAN="IP:${HOST},DNS:${HOST}"
    else
        SAN="DNS:${HOST}"
    fi
    openssl req -x509 -nodes -newkey rsa:2048 -days 3650 \
        -keyout "$CERT_DIR/key.pem" \
        -out    "$CERT_DIR/cert.pem" \
        -subj   "/C=EU/ST=Local/L=Local/O=ISMS CORE/CN=${HOST}" \
        -addext "subjectAltName=${SAN}" \
        2>/dev/null
    echo "[nginx/tls] Self-signed certificate generated (CN=${HOST}, SAN=${SAN}, valid 10yr)"
fi

# ── Render nginx config from template ────────────────────────────────────────
echo "[nginx/tls] Rendering nginx config (NGINX_HOST=${NGINX_HOST:-localhost})..."
envsubst '${NGINX_HOST}' \
    < /etc/nginx/templates/default.conf.template \
    > /etc/nginx/conf.d/default.conf

echo "[nginx/tls] Starting nginx..."
exec nginx -g 'daemon off;'
