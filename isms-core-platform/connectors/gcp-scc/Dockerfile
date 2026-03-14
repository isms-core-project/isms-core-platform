FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY gcp-scc/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY gcp-scc/connector.py gcp-scc/gcp_scc_client.py ./
CMD ["python", "connector.py"]
