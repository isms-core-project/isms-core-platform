FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY fortigate/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY fortigate/connector.py fortigate/fortigate_client.py ./
CMD ["python", "connector.py"]
