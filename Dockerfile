FROM python:3.10.12
# FROM selenium/standalone-chrome:latest


WORKDIR /twitter_scrape_bot

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY target_data.csv twitter_scrape_bot/target_data.csv

COPY . .

CMD ["python", "main.py"]
