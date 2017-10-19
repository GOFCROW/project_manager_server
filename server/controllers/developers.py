from xml.etree import ElementTree as ET
from ._main import CrudHandler
from ..logic_layer.developers import DeveloperLogic


class ListDev(CrudHandler):
    def post(self):
        self.list_objs(
            DeveloperLogic(self.db),
            'developers'
        )

class InsertDev(CrudHandler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        for child in xml:
            #TODO: Crear objeto Developer y insertar en la BD
            print(child.tag, child.attrib)

        #Developer = toobj(xml)
        # insertar los developers
        self.write('good')

class UpdateDev(CrudHandler):

    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # actualizar los developers
        self.write(xml)

class GetDev(CrudHandler):
    def post(self):
        self.get_obj(DeveloperLogic(self.db))
