FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY zabbix/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY zabbix/connector.py zabbix/zabbix_client.py ./

CMD ["python", "connector.py"]
