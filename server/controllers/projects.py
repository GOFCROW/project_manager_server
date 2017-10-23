from ..logic_layer.projects import ProjLogic
from ..data_layer.models import Project
from .handler import Handler
from .validation import cstr


class ListProj(Handler):
    def post(self, *args, **kwargs):
        self.list_objs(
            ProjLogic(self.db),
            'projects'
        )

class UpdateProj(Handler):
    schema = {
        'id': cstr(int, required=False),
        'name': cstr(str, 50),
        'description': cstr(str, 50),
        'estimated_hours': cstr(int),
        'enabled': cstr(bool, required=False),
        'assignments': {'type': 'list', 'schema':{
            'type': 'dict',
            'schema': {
                'hours_worked': cstr(int),
                'fk_role': cstr(int),
                'fk_dev': cstr(int)
            }
        }}
    }

    def post(self, *args, **kwargs):
        self.update_obj(
            self.schema,
            ProjLogic(self.db),
            Project
        )

class GetProj(Handler):
    def post(self):
        self.get_obj(ProjLogic(self.db))
