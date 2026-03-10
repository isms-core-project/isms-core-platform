<h1 align="center">🎋 ISMS CORE Platform — Getting Started</h1>

<p align="center">
  <strong>How to run the ISMS CORE Platform locally</strong>
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

> **Linux only:** OpenSearch requires `vm.max_map_count=262144`. If not already set:
> ```bash
> sudo sysctl -w vm.max_map_count=262144
> # Make permanent:
> echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
> ```

---

## Directory Layout

The Platform expects ISMS CORE content repositories to sit **alongside** the platform directory. The default layout:

```
/your/base/directory/
├── factory_isms/                    ← this repository (content + platform)
│   ├── platform/                    ← Platform source (docker-compose.yml lives here)
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
cp platform/.env.example platform/.env
```

Edit `platform/.env` and set the three required secrets:

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
cd platform
docker compose up -d
```

This starts 6 services: PostgreSQL, Redis, OpenSearch, Backend API, Celery Worker, and React Frontend.

**First boot takes longer** (~2–3 minutes) — OpenSearch needs to initialise before the backend will accept connections. Watch progress:

```bash
docker compose logs -f
```

All services healthy when you see no more errors and:
```
isms-core-backend  | INFO:     Application startup complete.
isms-core-frontend | ... ready in ... ms
```

### Step 4 — Verify services are running

```bash
docker compose ps
```

All six services should show `healthy` or `running`:

```
NAME                    STATUS          PORTS
isms-core-postgres      healthy         0.0.0.0:5432->5432/tcp
isms-core-redis         healthy         0.0.0.0:6379->6379/tcp
isms-core-opensearch    healthy         0.0.0.0:9200->9200/tcp
isms-core-backend       healthy         0.0.0.0:8000->8000/tcp
isms-core-worker        running
isms-core-frontend      running         0.0.0.0:3000->3000/tcp
```

**Health check endpoints:**
- Backend API: `http://localhost:8000/health`
- OpenSearch: `http://localhost:9200/_cluster/health`

---

## First Login

Open `http://localhost:3000` in your browser.

**Default admin credentials:**

| Field | Value |
|-------|-------|
| Email | `admin@isms-core.dev` |
| Password | `admin123` |

> ⚠️ **Change the admin password immediately after first login.** Go to Admin → Users → Edit.

---

## Initial Data Import

On first boot, the database is empty. You need to load the reference frameworks and import your ISMS content.

> All steps below can be run via the WebUI: **Admin → System → Initial Data Import section**. Use the API if you prefer scripting.

### 1. Load reference frameworks

The platform ships 18 pre-built reference framework bundles (ISO 27001, NIST CSF 2.0, MITRE ATT&CK v18, GDPR, DORA, NIS2, etc.).

```bash
# Authenticate first — get your token
TOKEN=$(curl -s -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@isms-core.dev","password":"admin123"}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

# Load all 18 framework bundles
curl -s -X POST http://localhost:8000/api/v1/admin/load \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
```

### 2. Import policies and implementation guides

```bash
# Import all policies (POL, OP-POL, INS, REF, CTX, FORM)
curl -s -X POST http://localhost:8000/api/v1/admin/import-policies \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"

# Import IMP documents (UG + TG) — also indexes into OpenSearch for full-text search
curl -s -X POST http://localhost:8000/api/v1/admin/import-implementations \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
```

### 3. Import assessment workbook structures

```bash
# Import 188 framework assessment workbook structures (from generator scripts)
curl -s -X POST http://localhost:8000/api/v1/admin/import-framework-workbooks \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"

# Import 53 operational compliance checklist structures
curl -s -X POST http://localhost:8000/api/v1/admin/import-operational \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"

# Import Privacy (ISO 27701) + Cloud (ISO 27018) compliance checklists
curl -s -X POST http://localhost:8000/api/v1/admin/import-privacy \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
```

### 4. Or run all importers in one shot

```bash
# Full sync — runs all importers (policies, IMPs, operational, privacy/cloud, workbooks) in sequence
curl -s -X POST http://localhost:8000/api/v1/sync/full \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"
```

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

## Production Deployment (NUC / Server)

For deployment on a dedicated server (e.g., nuc-01 at `10.0.0.110`):

### 1. Set strong secrets in `.env`

All three secrets **must** be changed from defaults. Use `openssl rand -hex 32` for each.

### 2. Set DEBUG=false

In `docker-compose.yml`, change the backend environment:
```yaml
- DEBUG=false
- LOG_LEVEL=WARNING
```

### 3. Configure CORS for your hostname

```yaml
- CORS_ORIGINS=https://your-domain.com,http://your-server-ip:3000
```

### 4. Restrict port exposure (optional)

For internal-only access, change port bindings to bind to localhost only:
```yaml
ports:
  - "127.0.0.1:5432:5432"   # PostgreSQL — localhost only
  - "127.0.0.1:6379:6379"   # Redis — localhost only
  - "127.0.0.1:9200:9200"   # OpenSearch — localhost only
  - "0.0.0.0:8000:8000"     # API — network accessible
  - "0.0.0.0:3000:3000"     # Frontend — network accessible
```

### 5. Data persistence

Docker volumes (`postgres-data`, `redis-data`, `opensearch-data`) are stored in `/var/lib/docker/volumes/` by default. On NUC deployments with a dedicated data disk (`/mnt/data`), specify custom volume paths:

```yaml
volumes:
  postgres-data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /mnt/data/isms-postgres
```

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

---

## API Documentation

The backend auto-generates OpenAPI documentation. Once running:

| URL | Description |
|-----|-------------|
| `http://localhost:8000/docs` | Swagger UI — interactive API explorer |
| `http://localhost:8000/redoc` | ReDoc — clean reference documentation |
| `http://localhost:8000/openapi.json` | Raw OpenAPI schema |

---

## Environment Variables Reference

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `POSTGRES_PASSWORD` | `change_this...` | **Yes** | PostgreSQL password |
| `REDIS_PASSWORD` | `change_this...` | **Yes** | Redis password |
| `SECRET_KEY` | `change_this...` | **Yes** | JWT signing secret (min 32 chars) |
| `ANTHROPIC_API_KEY` | *(empty)* | No | Required for ISMS Compass (Phase 8) |
| `POLICY_EXTRA_PATHS` | `/app/isms-cloud,/app/isms-privacy` | No | Comma-separated extra mount paths for Privacy + Cloud content |
| `DEBUG` | `true` | No | Set `false` in production |
| `LOG_LEVEL` | `INFO` | No | `DEBUG` / `INFO` / `WARNING` / `ERROR` |
| `CORS_ORIGINS` | `http://localhost:3000,...` | No | Comma-separated allowed origins |

---

<p align="center">
<strong>Copyright © 2025–2026 Gregory Griffin. All rights reserved.</strong>
</p>

<p align="center">
<em>Where bamboo antennas actually work.</em> 🎋
</p>
