import xml.etree.ElementTree as ET

class XmlHandler:
    def list_to_xml(self, list_, list_name):
        root = ET.Element(list_name)
        for e in list_:
            root.append(e.get_element())
        return ET.tostring(root)

    def xml_to_dict(self, xml_str: str):
        xml = ET.fromstring(xml_str)
        return self.xml_to_dict_(xml)

    def xml_to_dict_(self, xml: ET.Element):
        dict_ = dict()
        for x in xml:
            if len(x) < 1:
                dict_[x.tag] = x.text
            elif len(x) < 2 or x[0].tag == x[1].tag:
                dict_[x.tag] = [self.xml_to_dict_(item) for item in x]
            else:
                dict_[x.tag] = {x.tag: self.xml_to_dict_(item) for item in x}
        return dict_

    def wrap(self, text, tag):
        e = ET.Element(tag)
        e.text = text
        return ET.tostring(e)

    def unwrap(self, text: str):
        xml = ET.fromstring(text)
        return xml.text
