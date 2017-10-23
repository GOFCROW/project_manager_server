from ..logic_layer.developers import DevLogic
from ..data_layer.models import Developer
from .handler import Handler
from .validation import cstr


class ListDev(Handler):
    def post(self, *args, **kwargs):
        self.list_objs(
            DevLogic(self.db),
            'developers'
        )

class UpdateDev(Handler):
    schema = {
        'id': cstr(int, required=False),
        'first_name': cstr(str, 50),
        'last_name': cstr(str, 50),
        'phone_number': cstr(str, 50),
        'experience': cstr(str, 255),
        'skills': cstr(str, 255),
        'email': cstr(str, 100),
        'enabled': cstr(bool, required=False)
    }

    def post(self, *args, **kwargs):
        self.update_obj(
            self.schema,
            DevLogic(self.db),
            Developer
        )

class GetDev(Handler):
    def post(self, *args, **kwargs):
        self.get_obj(DevLogic(self.db))
