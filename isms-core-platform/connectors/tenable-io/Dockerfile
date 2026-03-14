FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY tenable-io/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY tenable-io/connector.py tenable-io/tenable_io_client.py ./
CMD ["python", "connector.py"]
