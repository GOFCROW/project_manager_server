from ..data_layer.repositories import DeveloperRepo
from ._main import Logic

class DeveloperLogic(Logic):
    def __init__(self, db):
        super().__init__(DeveloperRepo(db), db)

    def insert_devs(self, xml_str):
        return DeveloperRepo(self.db).insert_devs(xml_str)

    def update_dev(self, xml_str):
        return DeveloperRepo(self.db).update_dev(xml_str)