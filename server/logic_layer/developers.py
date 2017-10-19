from ..data_layer.repositories import DeveloperRepo
from ._main import Logic

class DeveloperLogic(Logic):
    def __init__(self, db):
        super().__init__(DeveloperRepo(db), db)
