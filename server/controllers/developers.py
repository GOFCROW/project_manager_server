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
        response = DeveloperLogic(self.db).insert_devs(xml_str)
        self.write(response)

class UpdateDev(CrudHandler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        response = DeveloperLogic(self.db).update_dev(xml_str)
        self.write(response)

class GetDev(CrudHandler):
    def post(self):
        self.get_obj(DeveloperLogic(self.db))
