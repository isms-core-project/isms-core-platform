FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY prtg/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY prtg/connector.py prtg/prtg_client.py ./

CMD ["python", "connector.py"]
