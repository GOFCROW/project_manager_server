from ..data_layer.repositories import RoleDevRepo
from . import Logic

class RoleDevLogic(Logic):
    def __init__(self, db):
        super().__init__(RoleDevRepo(db), db)
