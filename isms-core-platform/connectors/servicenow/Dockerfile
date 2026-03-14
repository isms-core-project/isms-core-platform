FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY servicenow/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY servicenow/connector.py servicenow/servicenow_client.py ./

CMD ["python", "connector.py"]
