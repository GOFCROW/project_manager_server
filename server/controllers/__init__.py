from tornado.web import RequestHandler, HTTPError


class Error404Handler(RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.write('error')

class Handler(RequestHandler):
    def get(self):
        self.post()

class Index(Handler):
    def post(self):
        self.write('GOF PROJECT')
