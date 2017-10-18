from xml.etree import ElementTree as ET
from ._main import Handler
from ..logic_layer.developers import DeveloperLogic


class ListDev(Handler):
    def post(self):
        logic = DeveloperLogic(self.db)
        devs = logic.list_()
        elements = self.list_to_xml(devs, 'developers')
        self.write(ET.tostring(elements))

class InsertDev(Handler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        for child in xml:
            #TODO: Crear objeto Developer y insertar en la BD
            print(child.tag, child.attrib)

        #Developer = toobj(xml)
        # insertar los developers
        self.write('good')

class UpdateDev(Handler):
    def post(self):
        xml_str = self.get_argument('xml', None)
        xml = ET.fromstring(xml_str)
        # actualizar los developers
        self.write(xml)

class GetDev(Handler):
    def post(self):
        id_ = self.get_id()
        logic = DeveloperLogic(self.db)
        dev = logic.find(id_)
        self.write(ET.dump(dev.get_element_tree()))
