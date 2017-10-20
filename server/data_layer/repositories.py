from sqlalchemy.orm import joinedload

from .models import (
    Assignment,
    Developer,
    RoleDev,
    Project
) 
from xml.etree import ElementTree as ET
import traceback

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

    def all(self):
        return self.db.query(Developer).\
            options(joinedload('assignments').joinedload('project'))

    def insert_devs(self, xml_str):
        try:
            xml = ET.fromstring(xml_str)
            i = 0
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
                self.db.add(developer)
                i += 1
            self.db.commit()
            messages = {
                0: "No se encontraron registros para insertar por lo menos a un desarrollador.",
                1: "Desarrollador registrado correctamente.",
            }
            return {"success": True, "message": messages.get(i, "Desarrolladores registrados correctamente.")}
        except Exception:
            self.db.rollback()
            print(traceback.format_exc())
            return {"success": False, "message": "Ocurrio un error al registrar al desarrollador",
                    "error_message": traceback.format_exc()}

    def update_dev(self, xml_str):
        try:
            xml = ET.fromstring(xml_str)
            i = 0
            for child in xml.iter('developer'):
                developer = DeveloperRepo(self.db).find(child.find('id').text)
                if child.find('first_name') is not None:
                    developer.first_name = child.find('first_name').text
                if child.find('last_name') is not None:
                    developer.last_name = child.find('last_name').text
                if child.find('phone') is not None:
                    developer.phone = child.find('phone').text
                if child.find('experience') is not None:
                    developer.experience = child.find('experience').text
                if child.find('skills') is not None:
                    developer.skills = child.find('skills').text
                if child.find('mail') is not None:
                    developer.mail = child.find('mail').text
                if child.find('password') is not None:
                    developer.password = child.find('password').text
                if child.find('fk_role') is not None:
                    developer.fk_role = child.find('fk_role').text
                i += 1
                self.db.merge(developer)
            self.db.commit()
            messages = {
                0: "No se encontraron registros para modificar por lo menos a un desarrollador.",
                1: "Desarrollador actualizado correctamente."
            }
            return {"success": True, "message": messages.get(i, "Desarrolladores actualizados correctamente.")}
        except Exception:
            self.db.rollback()
            print(traceback.format_exc())
            return {"success": False, "message": "Ocurrio un error al actualizar al desarrollador",
                    "error_message": traceback.format_exc()}

class ProjectRepo(Repository):
    def __init__(self, db):
        super().__init__(Project, db)
