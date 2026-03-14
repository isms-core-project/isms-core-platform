FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY entra-id/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY entra-id/connector.py entra-id/graph_client.py ./

CMD ["python", "connector.py"]
