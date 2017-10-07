from .controllers._main import Index

from .controllers.developers import (
    ListDev,
    GetDev,
    InsertDev,
    UpdateDev
)

from .controllers.projects import (
    ListProj,
    GetProj,
    InsertProj,
    UpdateProj
)

HANDLERS = [
    (r'/', Index),

    (r'/developers', ListDev),
    (r'/developers/get', GetDev),
    (r'/developers/insert', InsertDev),
    (r'/developers/update', UpdateDev),

    (r'/projects', ListProj),
    (r'/projects/get', GetProj),
    (r'/projects/insert', InsertProj),
    (r'/projects/update', UpdateProj)
]
