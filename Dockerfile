FROM python:3.10-slim
WORKDIR /home/flask

COPY .env .
COPY memory_test.py .
COPY app.py .
COPY requirements.txt .
RUN apt update && apt install -y gcc musl-dev gunicorn
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn -b 5000 app:app"]
