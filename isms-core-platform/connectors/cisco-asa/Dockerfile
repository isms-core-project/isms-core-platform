FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY cisco-asa/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY cisco-asa/connector.py cisco-asa/cisco_asa_client.py ./
CMD ["python", "connector.py"]
