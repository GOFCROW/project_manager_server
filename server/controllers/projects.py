from ..connection import DataBase
from xml.etree import ElementTree as ET
from ._main import Handler


class ListProj(Handler):
    def post(self):
        # listar los projectos
        self.write('Projs')

class InsertProj(Handler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # insertar los projectos
        self.write(xml)

class UpdateProj(Handler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # actualizar los projectos
        self.write(xml)

class GetProj(Handler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # obtener los projectos
        self.write(xml)
