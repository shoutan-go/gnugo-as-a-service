FROM debian:jessie

RUN apt-get update \
    && apt-get install -y git python-pip gnugo \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U flask \
    && pip install -U flask-cors \
    && pip install -U gomill

WORKDIR /usr/src

COPY . .

EXPOSE 5000
CMD ["python","gnugo-as-a-service.py","--host","0.0.0.0","--port","5000"]
