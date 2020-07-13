import os
import sys
from cli.cli import CLI
from web_server import create_app


def run():
    if sys.argv[1] == '-web':
        os.environ['FLASK_APP'] = 'ats_hacker.web_server:create_app()'
        create_app().run()
    else:
        cli = CLI()
        cli.start()
