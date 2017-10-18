# import hashlib
import sqlite3

from configparser import ConfigParser

from server import DataBase
from server.data_layer.models import (
    Base,
    Developer,
    RoleDev
)

config = ConfigParser()
config.read('settings.ini')
connection_string = config['Database']['url']
DataBase.set_engine(connection_string)

db_name = connection_string.split('///')[1]
sqlite3.connect(db_name)

Base.metadata.drop_all(DataBase.engine, checkfirst=True)
Base.metadata.create_all(DataBase.engine, checkfirst=True)

print(('Database and Tables') + 'dropped/created successfully!')

db = DataBase.get_session()

db.add(RoleDev(
    name = 'programador'
))
db.commit()

for i in range(0, 20):
    db.add(Developer(
        first_name='nombre' + str(i),
        last_name='apellido' + str(i),
        phone='123455' + str(i),
        experience='alto',
        skills='programar',
        mail='mail' + str(i),
        password='12345',
        fk_role=1
    ))
db.commit()

print('Default insertions done!')
