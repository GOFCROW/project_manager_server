from ..logic_layer.roles import RoleDevLogic
from .handler import Handler


class ListRoleDev(Handler):
    def post(self, *args, **kwargs):
        self.list_objs(
            RoleDevLogic(self.db),
            'roles'
        )
