FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && useradd -r -u 1000 -m -s /bin/false appuser \
    && mkdir -p /data/ti \
    && chown appuser:appuser /data/ti

COPY feeds/ /app/feeds/
COPY scheduler.py .
COPY trigger_server.py .

ENV PYTHONPATH=/app

RUN chown -R appuser:appuser /app
USER appuser

CMD ["python", "scheduler.py"]
