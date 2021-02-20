FROM python:3.8.8-alpine
RUN apk update
COPY requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /app

CMD ["python","main.py"]
