import json
from datetime import datetime, date, time
import xml.etree.ElementTree as ET

class Serializable:
    def __init__(self, **args):
        self.relationships = {
            r.key : r for r in self.__mapper__.relationships
        }

        for attr in args:
            value = args[attr]
            if attr in self.relationships:
                relation = self.relationships[attr]
                mapped_class = relation.mapper.class_
                if relation.uselist:
                    value = [mapped_class(**v) for v in value]
                else:
                    value = mapped_class(value)
            setattr(self, attr, value)

    def get_dict(self, processed: list = None):
        processed = list() if processed is None else processed
        processed.append(type(self))
        dict_ = dict(self.__dict__)
        dict_.pop('_sa_instance_state', None)
        relationships = self.__mapper__.relationships
        for relation in relationships:
            name = relation.key
            if name in dict_ and relation.mapper.class_ not in processed:
                value = dict_[name]
                if isinstance(value, list):
                    dict_[name] = [v.get_dict(processed[:]) for v in value]
                else:
                    if value is not None:
                        dict_[name] = value.get_dict(processed[:])
                    else:
                        dict_[name] = None
        return dict_

    def alchemy_encoder(self, obj):
        if isinstance(obj, (datetime, date, time)):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    def get_json(self):
        return json.dumps(self.get_dict(), default=self.alchemy_encoder)

    def get_element_tree(self, root=None):
        root = ET.Element(self.__class__.__name__) if root is None else root
        dict_ = self.get_dict()
        for attr in dict_:
            value = dict_[attr]
            if isinstance(value, list) and len(value) > 0:
                attr_list = ET.SubElement(root, attr)
                for obj in value:
                    obj.get_element_tree(attr_list)
            elif isinstance(value, dict):
                ET.SubElement(root, attr).append(value.get_element_tree())
            else:
                ET.SubElement(root, attr).text = str(dict_[attr])
        return root

    def get_xml(self):
        return ET.dump(self.get_element_tree())
