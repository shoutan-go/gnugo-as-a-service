# gnugo-as-a-service
A wrapper to use GnuGo through a webservice

## How to use

    python gnugo-as-a-service.py --host 127.0.0.1 --port 5000 -e /usr/games/gnugo &
    curl -d '(;FF[4]GM[1]SZ[9];B[ee];W[ge])' http://127.0.0.1:5000/score/estimate
    ...
