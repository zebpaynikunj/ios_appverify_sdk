# coding=utf-8

from bottle import default_app, run
from pygenjwt.generator import *

application = default_app()

if __name__ == '__main__':
    '''

    Runs when script is started directly from commandline
    '''
    run(host='localhost', port=8080, reloader=True)