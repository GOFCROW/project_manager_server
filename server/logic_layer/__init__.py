
class Logic:
    def __init__(self, repo, db):
        self.db = db
        self.repo = repo

    def all(self):
        return self.repo.all()

    def find(self, id_):
        return self.repo.find(id_)

    def insert(self, obj):
        self.repo.insert(obj)

    def update(self, obj):
        self.repo.update(obj)
