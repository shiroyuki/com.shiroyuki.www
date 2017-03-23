from gallium.interface import ICommand
from tornado.ioloop    import IOLoop


class HTTP(ICommand):
    def identifier(self):
        return 'http'

    def define(self, parser):
        pass

    def execute(self, args):
        print('Starting HTTP...')

        http_service       = self.core.get('http')
        http_service.debug = True

        try:
            IOLoop.current().start()
        except KeyboardInterrupt:
            print('Stopped HTTP.')
