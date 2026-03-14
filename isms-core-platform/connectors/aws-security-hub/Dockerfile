FROM python:3.12-slim
WORKDIR /app
COPY base /app/base
COPY aws-security-hub/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY aws-security-hub/connector.py aws-security-hub/aws_security_hub_client.py ./
CMD ["python", "connector.py"]
