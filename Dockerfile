FROM debian:stable

RUN apt-get update && apt-get -y install python3 python3-pip gunicorn

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt --break-system-packages

CMD ["/usr/bin/gunicorn", "app:app", "--bind", "0.0.0.0:54321", "--workers", "2"]
