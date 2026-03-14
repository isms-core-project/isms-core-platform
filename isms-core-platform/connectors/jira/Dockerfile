FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY jira/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY jira/connector.py jira/jira_client.py ./

CMD ["python", "connector.py"]
