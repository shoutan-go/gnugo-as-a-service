from flask import Flask, request
from flask.ext.cors import CORS
from gomill import sgf
import optparse
import subprocess
import os
import shutil
import tempfile

app = Flask(__name__)
CORS(app)

@app.route('/score/<string:method>', methods=['POST'])
def score(method):
    global options
    # create tmpfifo
    temppath = tempfile.mkdtemp()
    sgffile = '%s/game.sgf' % temppath;
    os.mkfifo(sgffile)
    gnugocmd = "%s --score %s -l %s" % (options.executable, method, sgffile)
    to_gnugo, from_gnugo = os.popen2(gnugocmd)
    # write info
    info = request.get_data(as_text=True);
    file = open(sgffile, "w")
    file.write(info);
    file.close();
    # read result
    line = from_gnugo.readline()
    # cleanup
    shutil.rmtree(temppath)
    return line, 200, {'Content-Type': 'application/text; charset=utf-8'}

if __name__ == '__main__':
    default_pathtognugo = '/usr/games/gnugo'
    default_host = "127.0.0.1"
    default_port = "5000"

    # Set up the command-line options
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host",
                      help="Hostname of the Flask app " + \
                           "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port",
                      help="Port for the Flask app " + \
                           "[default %s]" % default_port,
                      default=default_port)
    parser.add_option("-e", "--executable",
                      help="Path to the GnuGo executable " + \
                           "[default %s]" % default_pathtognugo,
                      default=default_pathtognugo)

    options, _ = parser.parse_args()

    app.run(
        host=options.host,
        port=int(options.port)
    )
