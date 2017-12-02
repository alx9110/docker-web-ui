""" Run server """
from webui.uwsgi import app


if __name__ == '__main__':
    app.run()
