FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY panw/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY panw/connector.py panw/panw_client.py ./
CMD ["python", "connector.py"]
