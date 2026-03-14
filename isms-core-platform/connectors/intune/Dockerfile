FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY intune/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY intune/connector.py intune/intune_client.py ./

CMD ["python", "connector.py"]
