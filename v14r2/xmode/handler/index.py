from imagination.standalone import container
from tornado.web import RequestHandler

from tori5.template import render

class Handler(RequestHandler):
    def get(self):
        self.finish(render('index.html', dict(name = "Panda")))
