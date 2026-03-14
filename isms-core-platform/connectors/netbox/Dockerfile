FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY netbox/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY netbox/connector.py netbox/netbox_client.py ./

CMD ["python", "connector.py"]
