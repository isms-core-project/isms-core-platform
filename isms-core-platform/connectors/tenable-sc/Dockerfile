FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY tenable-sc/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY tenable-sc/connector.py tenable-sc/tenable_sc_client.py ./
CMD ["python", "connector.py"]
