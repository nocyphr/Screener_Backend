FROM python:alpine

WORKDIR /app

COPY ./assets/api_requirements.txt .
RUN pip install --no-cache-dir -r api_requirements.txt

COPY . .

CMD ["python", "main.py"]
