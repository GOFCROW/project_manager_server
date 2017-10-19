from ..data_layer.repositories import ProjectRepo
from ._main import Logic

class ProjectLogic(Logic):
    def __init__(self, db):
        super().__init__(ProjectRepo(db), db)
