FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY sentinel/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sentinel/connector.py sentinel/sentinel_client.py ./

CMD ["python", "connector.py"]
