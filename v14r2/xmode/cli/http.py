from gallium.interface import ICommand

from imagination.standalone import container


class HTTP(ICommand):
    def identifier(self):
        return 'http'

    def define(self, parser):
        pass

    def execute(self, args):
        container.get('tori5.http.tornado.app') # Just to trigger app initialization.
        container.get('tori5.http.tornado').start()
