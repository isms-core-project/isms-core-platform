FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bridge.py .

# Non-root user for production
RUN useradd -r -s /bin/false bridge
USER bridge

CMD ["python", "bridge.py"]
