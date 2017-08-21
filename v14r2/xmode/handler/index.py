from tornado.web import RequestHandler


class Handler(RequestHandler):
    def get(self):
        self.finish("Hello, world")
