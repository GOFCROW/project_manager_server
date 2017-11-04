from sqlalchemy.orm import joinedload

from .models import (
    Developer,
    Project
)

class Repository:
    def __init__(self, entity, db):
        self.entity = entity
        self.db = db

    def find(self, id_):
        return self.db.query(self.entity).get(id_)

    def all(self):
        return self.db.query(self.entity).all()

    def update(self, obj):
        self.db.merge(obj)
        self.db.commit()


class DevRepo(Repository):
    def __init__(self, db):
        super().__init__(Developer, db)

    def all(self):
        return self.db.query(Developer).\
            options(joinedload('assignments').
                    joinedload('project'))


class ProjRepo(Repository):
    def __init__(self, db):
        super().__init__(Project, db)

    def all(self):
        return self.db.query(Project).\
            options(joinedload('assignments').
                    joinedload('developer'))
