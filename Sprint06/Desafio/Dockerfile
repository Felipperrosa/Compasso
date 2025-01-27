FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install boto3 pandas

CMD ["python", "upload_s3.py"]
