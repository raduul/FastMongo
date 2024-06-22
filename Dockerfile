# Dockerfile for the FastAPI app
FROM python:3.9-slim

WORKDIR /app

COPY ./api /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "run.py"]

