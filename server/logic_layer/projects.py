from ..data_layer.repositories import ProjRepo
from . import Logic

class ProjLogic(Logic):
    def __init__(self, db):
        super().__init__(ProjRepo(db), db)
