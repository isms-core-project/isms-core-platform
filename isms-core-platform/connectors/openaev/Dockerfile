FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY openaev/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY openaev/connector.py openaev/openaev_client.py ./
CMD ["python", "connector.py"]
