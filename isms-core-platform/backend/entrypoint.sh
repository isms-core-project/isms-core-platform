#!/bin/bash
# Backend entrypoint — runs Alembic migrations then starts uvicorn.
# On a fresh DB (init_db.sql bootstrapped but no alembic_version row):
#   stamps at 009_audit_log_phase9 then upgrades to head.
# On an existing DB: just upgrades to head (no-op if already at head).
set -e

echo "[entrypoint] Checking Alembic version..."
CURRENT=$(alembic current 2>/dev/null | grep -Eo '[a-z0-9_]+' | head -1 || echo "")

if [ -z "$CURRENT" ]; then
    echo "[entrypoint] Fresh DB — stamping at 009_audit_log_phase9 (init_db.sql baseline)..."
    echo "[entrypoint] Migrations 010-024 will run via upgrade head below."
    alembic stamp 009_audit_log_phase9
fi

echo "[entrypoint] Running alembic upgrade head..."
alembic upgrade head
echo "[entrypoint] Migrations complete."

exec uvicorn src.main:app --host 0.0.0.0 --port 8000
