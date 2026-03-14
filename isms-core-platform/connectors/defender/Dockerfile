FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY defender/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY defender/connector.py defender/defender_client.py ./

CMD ["python", "connector.py"]
