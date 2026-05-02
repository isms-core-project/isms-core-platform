FROM nginx:alpine

RUN apk add --no-cache openssl gettext

# Remove default config
RUN rm -f /etc/nginx/conf.d/default.conf

COPY nginx.conf.template /etc/nginx/templates/default.conf.template
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Default ports — Docker Compose keeps these (Docker grants NET_BIND_SERVICE by default).
# K8s manifests override to 8080/8443 (no capabilities needed, runs rootless).
ENV NGINX_HTTP_PORT=80 NGINX_HTTPS_PORT=443

# Pre-create runtime dirs owned by the nginx user (UID 101 on nginx:alpine).
# No USER directive here — Docker Compose runs as root (reads host-mounted certs fine).
# K8s enforces UID 101 via securityContext.runAsUser in the manifest (rootless Option B).
RUN chown -R nginx:nginx /etc/nginx /var/cache/nginx /var/log/nginx \
    && touch /var/run/nginx.pid \
    && chown nginx:nginx /var/run/nginx.pid

EXPOSE 80 443

ENTRYPOINT ["/entrypoint.sh"]
