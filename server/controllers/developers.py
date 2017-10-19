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
        DeveloperLogic(self.db).insert_devs(xml_str)
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
