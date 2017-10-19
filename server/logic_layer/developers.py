from ..data_layer.repositories import DeveloperRepo
from ._main import Logic

class DeveloperLogic(Logic):
    def __init__(self, db):
        super().__init__(DeveloperRepo(db), db)

    def insert_devs(self, xml_str):
        DeveloperRepo(self.db).insert_devs(xml_str)
