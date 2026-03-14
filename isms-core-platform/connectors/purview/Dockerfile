FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY purview/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY purview/connector.py purview/purview_client.py ./
CMD ["python", "connector.py"]
