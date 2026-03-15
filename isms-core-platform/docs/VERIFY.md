# ISMS CORE Platform — Verification Steps

## Prerequisites

- Docker Desktop running
- Terminal in `60-isms-core-api/`

## 1. Start the Stack

```bash
docker compose up -d
```

Wait for all services to be healthy:

```bash
docker compose ps
```

Expected: `isms-core-postgres`, `isms-core-redis`, `isms-core-opensearch`, `isms-core-backend`, `isms-core-worker`, `isms-core-frontend` all showing `healthy` or `running`.

If the backend isn't healthy yet, check logs:

```bash
docker compose logs isms-core-backend --tail 50
```

## 2. Health Check

```bash
curl http://localhost:8000/health
```

Expected:

```json
{"status": "ok", "database": "ok", "version": "1.0.0"}
```

## 3. Login (Get JWT)

```bash
curl -s -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@isms-core.dev", "password": "admin123"}' | python3 -m json.tool
```

Expected: `access_token`, `refresh_token`, `token_type: "bearer"`.

Save the access token:

```bash
TOKEN=$(curl -s -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@isms-core.dev", "password": "admin123"}' | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
```

## 4. List Frameworks

```bash
curl -s http://localhost:8000/api/v1/frameworks/ \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
```

Expected: 15 frameworks (ISO 27001, NIST CSF 2.0, NIST 800-53, CIS v8, MITRE ATT&CK, OWASP Top 10, OWASP ASVS, Swiss nFADP, EU GDPR, FINMA, NIS2, DORA, PCI DSS, EU AI Act, US CLOUD Act).

## 5. List Control Groups

```bash
curl -s http://localhost:8000/api/v1/controls/ \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool | head -40
```

Expected: 54 control groups (53 ISO Annex A + 1 Foundation group '00').

Filter by section:

```bash
curl -s "http://localhost:8000/api/v1/controls/?section=A.8" \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
```

Filter by product:

```bash
curl -s "http://localhost:8000/api/v1/controls/?product=operational" \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
```

## 6. Framework Controls

Pick an ISO 27001 framework ID from step 4, then:

```bash
curl -s "http://localhost:8000/api/v1/frameworks/{framework_id}/controls?level=1" \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool | head -40
```

Expected: 93 Annex A controls (level 1).

## 7. Cross-Framework Mappings

```bash
curl -s "http://localhost:8000/api/v1/frameworks/{framework_id}/mappings" \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool | head -40
```

Expected: Mappings from this framework to others.

## 8. System Status (Admin)

```bash
curl -s http://localhost:8000/api/v1/admin/sysinfo \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
```

Expected counts (approximate):

| Table | Count |
|-------|-------|
| frameworks | 15 |
| framework_controls | ~2,850 |
| cross_framework_mappings | ~2,127 (1,898 crosswalk + 229 control dependencies) |
| control_groups | 54 |
| policies | ~143 |
| implementations | ~376 |
| assessments | ~241 |

## 9. Load History

```bash
curl -s http://localhost:8000/api/v1/admin/load-history \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
```

Expected: 16 entries (1 per bundle), all with `load_status: "success"`.

## 10. Swagger UI

Open in browser: [http://localhost:8000/docs](http://localhost:8000/docs)

All API endpoints should be listed. Key routers: auth, controls, frameworks, assessments, dashboard, search, sync, admin, qa.

## 11. Frontend

Open in browser: [http://localhost:3000](http://localhost:3000)

Login with `admin@isms-core.dev` / `admin123`. Expected pages: Overview, Controls, Policies, Assessments, Coverage, Gaps, Evidence, QA, Admin, System.

## Teardown

```bash
docker compose down          # Stop containers
docker compose down -v       # Stop + delete volumes (full reset)
```

## Troubleshooting

| Symptom | Check |
|---------|-------|
| Backend won't start | `docker compose logs isms-core-backend` — look for import errors |
| Database "ok" but no frameworks | Check seed logs: `docker compose logs isms-core-backend \| grep -i seed` |
| 401 on authenticated endpoints | Token expired (60 min). Re-run step 3. |
| PostgreSQL won't start | Volume conflict from old schema. Run `docker compose down -v` for clean start. |
| Redis health check fails | Password mismatch. Check `REDIS_PASSWORD` in `.env` vs compose. |
