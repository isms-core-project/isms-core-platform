FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY active-directory/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY active-directory/connector.py active-directory/ldap_client.py ./

CMD ["python", "connector.py"]
