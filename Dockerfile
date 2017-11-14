FROM debian:jessie

RUN apt-get update \
    && apt-get install -y git python-pip gnugo \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U flask \
    && pip install -U flask-cors
    && pip install -U gomill

RUN git clone https://github.com/shoutan-go/gnugo-as-a-service.git /opt/gnugo-as-a-service

WORKDIR /opt/gnugo-as-a-service

EXPOSE 5000
CMD ["python","gnugo-as-a-service.py","--host","0.0.0.0","--port","5000"]
