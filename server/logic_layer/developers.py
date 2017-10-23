from ..data_layer.repositories import DevRepo
from . import Logic

class DevLogic(Logic):
    def __init__(self, db):
        super().__init__(DevRepo(db), db)
