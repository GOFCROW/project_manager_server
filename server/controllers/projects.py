from xml.etree import ElementTree as ET

from ..logic_layer.projects import ProjectLogic
from ._main import CrudHandler


class ListProj(CrudHandler):
    def post(self):
        self.list_objs(
            ProjectLogic(self.db),
            'projects'
        )

class InsertProj(CrudHandler):

    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # insertar los projectos
        self.write(xml)

class UpdateProj(CrudHandler):

    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # actualizar los projectos
        self.write(xml)

class GetProj(CrudHandler):
    def post(self):
        self.get_obj(ProjectLogic(self.db))
