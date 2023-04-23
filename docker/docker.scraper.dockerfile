FROM python:alpine

WORKDIR /app

COPY ./assets/scraper_requirements.txt .
RUN pip install --no-cache-dir -r scraper_requirements.txt

CMD ["python", "./src/main.py"]
