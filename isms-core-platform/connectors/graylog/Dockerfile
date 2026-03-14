FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY graylog/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY graylog/connector.py graylog/graylog_client.py ./

CMD ["python", "connector.py"]
