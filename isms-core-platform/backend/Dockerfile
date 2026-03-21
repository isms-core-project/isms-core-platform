FROM python:3.11-slim

LABEL maintainer="ISMS CORE"
LABEL description="ISMS CORE Platform API"
LABEL version="1.0.0"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -r -u 1000 -m -s /bin/false appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/isms-data /app/assessments /app/datasets \
    /app/cache /app/uploads /app/logs \
    && chown -R appuser:appuser /app

HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER appuser

CMD ["/entrypoint.sh"]
