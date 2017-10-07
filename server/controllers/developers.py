from ..connection import DataBase
from xml.etree import ElementTree as ET
from ._main import Handler


class ListDev(Handler):
    def post(self):
        # listar los developers
        self.write('devs')

class InsertDev(Handler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # insertar los developers
        self.write(xml)

class UpdateDev(Handler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # actualizar los developers
        self.write(xml)

class GetDev(Handler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # obtener los developers
        self.write(xml)
