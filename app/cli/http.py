from gallium.interface import ICommand

from tornado.wsgi   import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web    import Application, FallbackHandler

from app.main import app as flask_app


class HTTP(ICommand):
    def identifier(self):
        return 'http'

    def define(self, parser):
        pass

    def execute(self, args):
        print('[HTTP] Service initializing...')

        app = Application(
            [
                (r".*", FallbackHandler, dict(fallback = WSGIContainer(flask_app))),
            ],
            debug = True
        )

        app.listen(8000, '0.0.0.0')

        try:
            print('[HTTP] Service listening...')
            IOLoop.current().start()
        except KeyboardInterrupt:
            print('\r[HTTP] Received termination')

        print('[HTTP] Service stopped')
