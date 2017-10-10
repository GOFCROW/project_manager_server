# import hashlib
import sqlite3

from configparser import ConfigParser

from server import DataBase
from server.data_layer.models import (
    Base
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
