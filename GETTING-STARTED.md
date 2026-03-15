<h1 align="center">🎋 ISMS CORE Platform — Getting Started</h1>

<p align="center">
  <strong>How to deploy and run the ISMS CORE Platform</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Docker-24%2B-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker 24+"/>
  <img src="https://img.shields.io/badge/Docker_Compose-v2-2496ED?style=flat-square" alt="Docker Compose v2"/>
  <img src="https://img.shields.io/badge/RAM-4GB_min-FF6600?style=flat-square" alt="4GB RAM"/>
  <img src="https://img.shields.io/badge/Disk-10GB_min-FF6600?style=flat-square" alt="10GB Disk"/>
</p>

---

## Prerequisites

| Requirement | Minimum | Notes |
|-------------|---------|-------|
| **Docker** | 24+ | `docker --version` to verify |
| **Docker Compose** | v2 (plugin) | `docker compose version` — note: `compose` not `compose-plugin` |
| **RAM** | 4 GB available | OpenSearch requires ~1.5 GB alone |
| **Disk** | 10 GB free | PostgreSQL + OpenSearch + images |
| **OS** | Linux, macOS, or Windows (WSL2) | Native Linux or macOS recommended |
| **nginx** | — | Production: nginx handles TLS on ports 80/443 automatically. No separate nginx install needed — it's a Docker container. |

> **Linux only:** OpenSearch requires `vm.max_map_count=262144`. If not already set:
> ```bash
> sudo sysctl -w vm.max_map_count=262144
> # Make permanent:
> echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
> ```

> **Production vs Development:**
> - **Production** (recommended): access via `https://{HOST_IP}` — nginx handles TLS automatically.
> - **Development**: backend on `:8000`, frontend on `:3000`, no TLS. For local development only.
>
> This guide covers **production deployment**. For development, use `docker-compose.yml` (no nginx) from the platform source.

---

## Directory Layout

The Platform expects ISMS CORE content repositories to sit **alongside** the platform directory. The default layout:

```
/your/base/directory/
├── factory_isms/                    ← this repository (content + platform)
│   ├── isms-core-platform/                    ← Platform source (docker-compose.yml lives here)
│   ├── isms-core-framework/         ← FRAMEWORK content (mounted read-only)
│   ├── isms-core-operational/       ← OPERATIONAL content (mounted read-only)
│   ├── isms-core-privacy/           ← PRIVACY content — ISO 27701:2025 (mounted read-only)
│   └── isms-core-cloud/             ← CLOUD content — ISO 27018:2025 (mounted read-only)
```

The `docker-compose.yml` mounts all four product directories as read-only volumes. **The platform never modifies these files.**

---

## Setup

### Step 1 — Clone the repository

```bash
git clone https://github.com/isms-core-project/factory_isms.git
cd factory_isms
```

### Step 2 — Create your `.env` file

```bash
cp isms-core-platform/.env.example isms-core-platform/.env
```

Edit `isms-core-platform/.env` and set the three required secrets:

```dotenv
# Required — change all three before running
POSTGRES_PASSWORD=your_strong_database_password
REDIS_PASSWORD=your_strong_redis_password
SECRET_KEY=your_random_secret_key_min_32_chars

# Optional — only needed for ISMS Compass (Phase 8, AI gap analysis)
ANTHROPIC_API_KEY=
```

> **Generating a strong SECRET_KEY:**
> ```bash
> python3 -c "import secrets; print(secrets.token_hex(32))"
> # or
> openssl rand -hex 32
> ```

### Step 3 — Start the stack

```bash
cd isms-core-platform
docker compose up -d
```

This starts 8 services: PostgreSQL, Redis, OpenSearch, Backend API, Celery Worker, Celery Beat, nginx, and React Frontend.

**First boot takes longer** (~2–3 minutes) — OpenSearch needs to initialise before the backend will accept connections. Watch progress:

```bash
docker compose logs -f
```

All services healthy when you see no more errors and:
```
isms-core-backend  | INFO:     Application startup complete.
isms-core-nginx    | ... start worker processes
```

### Step 4 — Verify services are running

```bash
docker compose ps
```

All eight services should show `healthy` or `running`:

```
NAME                    STATUS          PORTS
isms-core-postgres      healthy         0.0.0.0:5432->5432/tcp
isms-core-redis         healthy         0.0.0.0:6379->6379/tcp
isms-core-opensearch    healthy         0.0.0.0:9200->9200/tcp
isms-core-backend       healthy         0.0.0.0:8000->8000/tcp
isms-core-worker        running
isms-core-beat          Up
isms-core-nginx         healthy         0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp
isms-core-frontend      running         0.0.0.0:3000->3000/tcp
```

> **Note:** `isms-core-beat` shows no healthcheck status — just "Up". This is normal. Celery Beat runs no web server, so there is nothing to health-check. "Up" is correct.

**Health check endpoints:**
- Backend API: `http://localhost:8000/health`
- OpenSearch: `http://localhost:9200/_cluster/health`

---

## First Login

Open `https://{HOST_IP}` in your browser (replace with your server IP or FQDN).

**Self-signed certificate warning:** On first access, your browser will warn about the certificate. This is expected — nginx auto-generates a self-signed cert on first boot. Click "Advanced" → "Proceed" (Chrome) or "Accept the Risk" (Firefox). See [PLATFORM.md](PLATFORM.md) for TLS upgrade options.

**Default admin credentials are set in your `.env`:**
- Email: value of `ADMIN_EMAIL`
- Password: value of `ADMIN_PASSWORD`

---

## Initial Data Import

Run `bootstrap.sh` once after first boot. It handles everything automatically:

```bash
chmod +x bootstrap.sh
bash bootstrap.sh
```

The script: waits for the stack to be healthy → authenticates → runs all 6 import steps in the correct order → shows import stats on completion.

**Import order (handled automatically by bootstrap.sh):**
1. `POST /admin/load` — seeds ISMS control groups (must run first)
2. `POST /admin/import-policies`
3. `POST /admin/import-implementations`
4. `POST /admin/import-operational`
5. `POST /admin/import-privacy`
6. `POST /admin/import-framework-workbooks`
7. `POST /admin/reindex`

> ⚠️ **Do not skip bootstrap.sh.** If importers run before `/admin/load`, all content will be misrouted to wrong control groups.

**Re-running is safe** — all importers are idempotent (content-hashed, only changed files re-processed).

---

## After Import — What You'll See

| Section | What's there |
|---------|-------------|
| **Dashboard** | Compliance overview, audit readiness score, top gaps; ISMS / Privacy / Cloud product switcher |
| **Controls** | 87 control groups (54 ISMS + 21 Privacy + 12 Cloud) with policy/assessment/gap status |
| **Policies** | Imported documents (POL + OP-POL + PRIV-POL + CLD-POL + foundation + REF/CTX/INS) |
| **Assessments** | 188 framework + 53 operational + 21 privacy + 12 cloud workbook structures with per-item compliance status |
| **Gaps** | Identified compliance gaps — create, assign, track |
| **Evidence** | Upload and link evidence to control groups and requirements |
| **Coverage** | Heatmap of Framework and Operational coverage |
| **QA** | Existence checker — validates artifact completeness across all four products |
| **NIST CSF 2.0** | Assessment tool — 106 subcategories, tier ratings, gap report, XLSX import/export |
| **NIS2 / DORA / CIS Controls v8** | Regulatory assessment tools — maturity scoring 0–4, grouped by article/chapter/control |
| **Admin** | User management, system health, import controls |

---

## Stopping and Restarting

```bash
# Stop all services (data is preserved in Docker volumes)
docker compose down

# Stop and remove all data (full reset — WARNING: destroys database)
docker compose down -v

# Restart a single service
docker compose restart isms-core-backend

# View logs for a specific service
docker compose logs -f isms-core-backend
docker compose logs -f isms-core-worker
```

---

## Re-sync Content

When ISMS CORE content files are updated (new policies, revised workbooks), re-run the relevant importer:

```bash
# Re-sync all content (policies + IMPs + workbooks)
curl -s -X POST http://localhost:8000/api/v1/sync/full \
  -H "Authorization: Bearer $TOKEN"

# Or via WebUI: Admin → System → Re-sync
```

The importer uses content hashing — only changed files are re-processed.

---

## Production Deployment

See [PLATFORM.md](PLATFORM.md) for the complete production deployment guide including nginx TLS setup, `bootstrap.sh` usage, email profiles, and Go-Live Checklist.

---

## Troubleshooting

### OpenSearch fails to start

```
max virtual memory areas vm.max_map_count [65530] is too low
```

Fix:
```bash
sudo sysctl -w vm.max_map_count=262144
```

### Backend stuck in restart loop — "could not connect to server"

PostgreSQL or Redis hasn't started yet. Wait 30 seconds and check:
```bash
docker compose ps      # Are postgres/redis healthy?
docker compose logs isms-core-postgres
```

### Import returns 401 Unauthorized

Your token has expired (1 hour default). Re-authenticate:
```bash
TOKEN=$(curl -s -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@isms-core.dev","password":"admin123"}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
```

### Workbook import finds 0 files

Check that all content directories are correctly mounted. Verify inside the container:
```bash
docker exec isms-core-backend ls /app/isms-framework
docker exec isms-core-backend ls /app/isms-operational
docker exec isms-core-backend ls /app/isms-privacy
docker exec isms-core-backend ls /app/isms-cloud
```

If empty, check the volume mounts in `docker-compose.yml` point to the correct paths on your host. Also ensure `POLICY_EXTRA_PATHS=/app/isms-cloud,/app/isms-privacy` is set in your `.env` file.

### Frontend shows "Network Error" on all API calls

The Vite dev server proxies `/api` to the backend. Verify the backend is healthy:
```bash
curl http://localhost:8000/health
```

If the backend container is still starting, wait for it to be healthy and reload the browser.

### beat container shows no healthcheck status (just "Up")

Normal — the beat healthcheck is intentionally disabled. Celery Beat runs no web server, so there's nothing to health-check. "Up" is correct.

---

## API Documentation

The backend auto-generates OpenAPI documentation. Once running:

| URL | Description |
|-----|-------------|
| `https://{HOST_IP}/api/docs` | Swagger UI — interactive API explorer |
| `https://{HOST_IP}/api/redoc` | ReDoc — clean reference documentation |
| `https://{HOST_IP}/api/openapi.json` | Raw OpenAPI schema |

---

## Environment Variables Reference

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `POSTGRES_PASSWORD` | `change_this...` | **Yes** | PostgreSQL password |
| `REDIS_PASSWORD` | `change_this...` | **Yes** | Redis password |
| `SECRET_KEY` | `change_this...` | **Yes** | JWT signing secret (min 32 chars) |
| `ADMIN_EMAIL` | `admin@isms-core.dev` | No (has default) | Admin account email — created/updated on startup |
| `ADMIN_PASSWORD` | *(no default in prod)* | **Yes (prod)** | Admin account password — no default in production |
| `ANTHROPIC_API_KEY` | *(empty)* | No | Required for ISMS Compass (Phase 8) |
| `CONNECTORS_WORKER_SECRET` | *(empty)* | No | Shared secret for connector runner |
| `FQDN` | *(empty)* | No | Domain for Let's Encrypt TLS (leave empty for self-signed) |
| `HOST_IP` | *(your server IP)* | No | Server IP for nginx SAN + VITE_BACKEND_URL |
| `MAIL_HOST` | *(empty)* | No | `isms-core-mailhog` (Mailpit profile) or `isms-core-smtp-bridge` |
| `MAIL_PORT` | `1025` | No | SMTP port (default 1025 for both email profiles) |
| `POLICY_EXTRA_PATHS` | `/app/isms-cloud,/app/isms-privacy` | No | Comma-separated extra mount paths for Privacy + Cloud content |
| `DEBUG` | `true` | No | Set `false` in production |
| `LOG_LEVEL` | `INFO` | No | `DEBUG` / `INFO` / `WARNING` / `ERROR` |
| `CORS_ORIGINS` | `http://localhost:3000,...` | No | Comma-separated allowed origins |

---

<p align="center">
<strong>Copyright © 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>

<p align="center">
<em>Where bamboo antennas actually work.</em> 🎋
</p>
