import os
import sys

from gallium.interface      import IExtension
from imagination.loader     import Loader
from imagination.standalone import container as standalone_container
from tornado.web            import URLSpec

_shared = {'container': None}


def render(name, context):
    target = _shared['container'].get('tori5.template').get_template(name)

    return target.render(context)


class Extension(IExtension):
    loader_setup_map = {
        'fs' : {
            'class'      : 'jinja2.FileSystemLoader',
            'path_param' : 'searchpath',
        },
        'package' : {
            'class'      : 'jinja2.PackageLoader',
            'path_param' : 'package_name',
        },
    }
    def config_key(self):
        return 'template'

    def default_settings(self):
        return {
            'standalone'  : True,
            'auto_reload' : False,
            'type'        : None,
            'path'        : None,
        }

    def initialize(self, core, config):
        global _shared

        # NOTE As this is an experiment to work with the standalone, the given core may be ignored.
        container = standalone_container if config['standalone'] else core.container

        _shared['container'] = container

        if not config['type'] and not config['path'] and os.path.exists('templates'):
            config.update({
                'type': 'fs',
                'path': 'templates',
            })

        loader_type = str(config['type'] or '').lower()
        loader_path = str(config['path'] or '').lower()

        assert loader_type, 'The type of the template loader "{}" is not defined.'.format(alias)
        assert loader_path, 'The path of the template loader "{}" is not defined.'.format(alias)

        loader_class = None

        assert loader_type in self.loader_setup_map, 'The "{}" type of the template loader "{}" is not defined.'.format(loader_type, alias)

        loader_setup = self.loader_setup_map[loader_type]

        with container.define_entity('tori5.template.loader', loader_setup['class']) as sub_loader:
            sub_loader.set_param('str', loader_path, loader_setup['path_param'])

        with container.define_entity('tori5.template.autoescape', 'jinja2.select_autoescape') as autoescape:
            autoescape.set_param('list', ['html', 'xml'])

        environment_fqcn = 'jinja2.Environment'

        with container.define_entity('tori5.template', environment_fqcn) as template:
            template.add_dependency('tori5.template.loader',     'loader')
            template.add_dependency('tori5.template.autoescape', 'autoescape')

            if sys.version_info >= (3, 6, 0):
                template.set_param('bool', True, 'enable_async')
