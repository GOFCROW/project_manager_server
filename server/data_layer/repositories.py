from .models import Developer, Project
from xml.etree import ElementTree as ET

class Repository:
    def __init__(self, entity, db):
        self.entity = entity
        self.db = db

    def find(self, id_):
        return self.db.query(self.entity).get(id_)

    def all(self):
        return self.db.query(self.entity).all()

    def insert(self, obj):
        self.db.add(obj)
        self.db.commit()

    def update(self, obj):
        self.db.merge(obj)
        self.db.commit()

    def insert_all(self, objs):
        for obj in objs:
            self.db.add(obj)
        self.db.commit()

    def update_all(self, objs):
        for obj in objs:
            self.db.merge(obj)
        self.db.commit()

class DeveloperRepo(Repository):
    def __init__(self, db):
        super().__init__(Developer, db)

    def listar_dev_habilitado(self):
        return self.db.query(Developer).filter(Developer.enabled.is_(True)).all()

    def insert_devs(self, xml_str):
        xml = ET.fromstring(xml_str)
        for child in xml.iter('developer'):
            developer = Developer(
                first_name=child.find('first_name').text,
                last_name=child.find('last_name').text,
                phone=child.find('phone').text,
                experience=child.find('experience').text,
                skills=child.find('skills').text,
                mail=child.find('mail').text,
                password=child.find('password').text,
                fk_role=child.find('fk_role').text
            )
            self.db.merge(developer)
        self.db.commit()

class ProjectRepo(Repository):
    def __init__(self, db):
        super().__init__(Project, db)
