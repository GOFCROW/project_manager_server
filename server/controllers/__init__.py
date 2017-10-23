from tornado.web import RequestHandler, HTTPError


class Error404Handler(RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.write('Url inexistente, volver /')
        self.finish()

    def data_received(self, chunk):
        pass

class Index(RequestHandler):
    def get(self, *args, **kwargs):
        self.post()

    def post(self, *args, **kwargs):
        self.render('main.html')

    def data_received(self, chunk):
        pass
