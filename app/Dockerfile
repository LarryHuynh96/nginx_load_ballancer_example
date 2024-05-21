FROM python:3.8-slim

WORKDIR /app

COPY . .


RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:5000 wsgi:app --timeout 60
