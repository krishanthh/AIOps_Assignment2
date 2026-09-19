FROM python:3.12-slim

WORKDIR /app

COPY validate.py .
COPY shards /data

CMD ["python3", "validate.py"]