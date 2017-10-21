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

    def alchemy_encoder(self, obj):
        if isinstance(obj, (datetime, date, time)):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    def get_element(self, processed: list = None):
        processed = list() if processed is None else processed
        processed.append(type(self))
        dict_ = dict(self.__dict__)
        dict_.pop('_sa_instance_state', None)
        relationships = self.__mapper__.relationships
        root = ET.Element(self.__class__.__name__)

        for relation in relationships:
            name = relation.key
            if name in dict_ and relation.mapper.class_ not in processed:
                value = dict_[name]
                if isinstance(value, list):
                    if len(value) > 0:
                        subelement = ET.SubElement(root, name)
                        for v in value:
                            subelement.append(v.get_element(processed[:]))
                else:
                    if value is not None:
                        root.append(value.get_element(processed[:]))
                del(dict_[name])

        for attr in dict_:
            ET.SubElement(root, attr).text = str(dict_[attr])
        return root
