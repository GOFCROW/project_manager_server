from tornado.web import RequestHandler

from ..data_layer.connection import DataBase

class DataBaseHandler(RequestHandler):
    db = None

    def initialize(self):
        self.db = DataBase.get_session()

    def get(self, *args, **kwargs):
        self.post()

    def on_finish(self):
        self.db.close()

    def data_received(self, chunk):
        pass
