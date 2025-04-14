FROM python:3.10-slim

WORKDIR /app

COPY send_metrics.py .

RUN pip install requests

CMD ["python", "send_metrics.py"]

