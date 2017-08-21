from gallium.interface      import IExtension
from imagination.loader     import Loader
from imagination.standalone import container as standalone_container
from tornado.web            import URLSpec


class Extension(IExtension):
    def config_key(self):
        return 'http'

    def default_settings(self):
        return {
            'standalone'  : True,
            'handlers'    : [],
            'debug'       : False,
            'auto_reload' : False,
            'port'        : 8000,
        }

    def initialize(self, core, config):
        # NOTE As this is an experiment to work with the standalone, the given core may be ignored.
        container = standalone_container if config['standalone'] else core.container

        assert config['handlers'], 'The handlers is not defined.'

        routes = []

        for name, route in config['handlers'].items():
            assert 'pattern' in route, '"pattern" is not defined for route "{}".'.format(name)
            assert 'handler' in route, '"handler" is not defined for route "{}".'.format(name)

            routes.append(URLSpec(
                name    = name,
                pattern = route['pattern'],
                handler = Loader(route['handler']).package,
            ))

        with container.define_entity('tori5.http.tornado.app', 'tornado.web.Application') as app:
            app.set_param('list', routes,                'handlers')
            app.set_param('bool', config['debug'],       'debug')
            app.set_param('bool', config['auto_reload'], 'autoreload')

            with app.call('listen') as initial_call:
                initial_call.with_param('int', config['port'], 'port')

        with container.define_lambda('tori5.http.tornado.ioloop', 'tornado.ioloop.IOLoop'):
            pass # no parameters required

        with container.define_factorization('tori5.http.tornado', 'tori5.http.tornado.ioloop', 'current') as current_ioloop:
            pass # no parameters required
