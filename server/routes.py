from .controllers import Index
from .controllers.developers import (
    UpdateDev,
    ListDev
)

from .controllers.projects import (
    UpdateProj,
    ListProj
)

HANDLERS = [
    (r'/', Index),

    (r'/developers', ListDev),
    (r'/developers/update', UpdateDev),

    (r'/projects', ListProj),
    (r'/projects/update', UpdateProj)
]
