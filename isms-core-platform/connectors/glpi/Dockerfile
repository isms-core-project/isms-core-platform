FROM python:3.12-slim

WORKDIR /app

# Base class
COPY base /app/base

# Connector
COPY glpi/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY glpi/connector.py glpi/glpi_client.py ./

CMD ["python", "connector.py"]
