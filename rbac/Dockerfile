FROM python:3.10-slim

RUN pip install kubernetes

COPY get_secrets.py /app/get_secrets.py

CMD ["python", "/app/get_secrets.py"]
