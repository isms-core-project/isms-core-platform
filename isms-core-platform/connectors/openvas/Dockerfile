FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY openvas/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY openvas/connector.py openvas/openvas_client.py ./
CMD ["python", "connector.py"]
