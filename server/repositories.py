from .models import Developer, Project

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

class ProjectRepo(Repository):
    def __init__(self, db):
        super().__init__(Project, db)
