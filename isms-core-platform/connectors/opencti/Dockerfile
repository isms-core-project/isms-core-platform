FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY opencti/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY opencti/connector.py opencti/opencti_client.py ./
CMD ["python", "connector.py"]
