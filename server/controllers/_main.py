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
            root.append(e.get_element())
        return root

    def get_id(self):
        id_ = self.get_argument('id', None)
        if id_ is not None:
            try:
                return int(ET.fromstring(id_).text)
            except:
                self.write('invalid xml/data format, <req>int</req> expected!')
        else:
            self.write('id is required!')
        self.finish()


class CrudHandler(Handler):
    def list_objs(self, logic, plural_name):
        objs = logic.all()
        elements = self.list_to_xml(objs, plural_name)
        str_res = ET.tostring(elements)
        self.write(str_res)

    def get_obj(self, logic):
        id_ = self.get_id()
        obj = logic.find(id_)
        element = obj.get_element_tree()
        self.write(ET.tostring(element))


class Index(Handler):
    def get(self):
        self.render('main.html')
