FROM python:alpine

WORKDIR /app

COPY ./assets/api_requirements.txt .
RUN pip install --no-cache-dir -r api_requirements.txt

CMD ["python", "main.py"]
