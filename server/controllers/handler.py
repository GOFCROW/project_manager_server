from cerberus import Validator

from .database_handler import DataBaseHandler
from .xml_handler import XmlHandler

class Handler(DataBaseHandler, XmlHandler):
    def list_objs(self, logic, plural_name):
        objs = logic.all()
        xml = self.list_to_xml(objs, plural_name)
        self.write(xml)

    def get_obj(self, logic):
        id_ = self.get_id()
        obj = logic.find(id_)
        xml = obj.get_xml()
        self.write(xml)

    def update_obj(self, schema, logic, entity):
        dict_ = self.get_args_as_dict()
        v = Validator(schema)
        if v.validate(dict_):
            obj = entity(**v.document)
            logic.update(obj)
            self.write_mssg('ok')
        else:
            self.write_xml_error(v.errors)

    def write_xml_error(self, error):
        self.write(self.wrap(str(error), 'error'))

    def write_mssg(self, mssg):
        self.write(self.wrap(str(mssg), 'mssg'))

    def get_id(self):
        id_ = self.get_argument('id', None)
        if id_ is not None:
            try:
                return int(self.unwrap(id_))
            except:
                self.write_xml_error(
                    'invalid xml/data format, <req>int</req> expected!')
        else:
            self.write_xml_error('id is required!')
        self.finish()

    def get_args_as_dict(self):
        try:
            return self.xml_to_dict(self.request.body)
        except:
            self.write_xml_error('Invalid xml')
