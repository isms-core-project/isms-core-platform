FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY qualys/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY qualys/connector.py qualys/qualys_client.py ./
CMD ["python", "connector.py"]
