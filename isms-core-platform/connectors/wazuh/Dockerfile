FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY wazuh/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY wazuh/connector.py wazuh/wazuh_client.py ./

CMD ["python", "connector.py"]
