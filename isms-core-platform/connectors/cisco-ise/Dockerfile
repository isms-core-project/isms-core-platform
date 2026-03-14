FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY cisco-ise/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY cisco-ise/connector.py cisco-ise/cisco_ise_client.py ./
CMD ["python", "connector.py"]
