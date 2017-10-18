from tornado.web import RequestHandler, HTTPError
from ..data_layer.connection import DataBase
import xml.etree.ElementTree as ET


class Error404Handler(RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.write('error')

    def data_received(self, chunk):
        pass

class Handler(RequestHandler):
    db = None

    def initialize(self):
        self.db = DataBase.get_session()

    def get(self):
        self.post()

    def on_finish(self):
        self.db.close()

    def data_received(self, chunk):
        pass

    def list_to_xml(self, list_, list_name):
        root = ET.Element(list_name)
        for e in list_:
            root.append(e.get_element_tree())
        return root

    def get_id(self):
        id_ = self.get_argument('id', None)
        if id_ is not None:
            try:
                return int(ET.fromstring(id_)[0].text)
            except:
                self.write('invalid xml/data format!')
        else:
            self.write('id is required!')
        self.finish()

class Index(Handler):
    def post(self):
        self.write('GOF PROJECT')
