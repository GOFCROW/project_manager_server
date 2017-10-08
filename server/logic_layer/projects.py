from ..data_layer.repositories import ProjectRepo
from ._main import Logic

class ProjectLogic(Logic):
    def __init__(self, db):
        super().__init__(ProjectRepo(db), db)

    def all(self):
        #implementar logica de negocio
        return self.repo.all()

    def find(self, obj):
        #implementar logica de negocio
        return self.repo.find(obj)

    def insert(self, obj):
        #implementar logica de negocio
        self.repo.insert(obj)

    def update(self, obj):
        #implementar logica de negocio
        self.repo.update(obj)
