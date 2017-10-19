# import hashlib
import sqlite3
import random

from configparser import ConfigParser
from faker import Faker

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

FAKER = Faker()
years_exp = [
    'menos de 2 año',
    'de 2 - 4 años',
    'de 4 - 7 años',
    'de 7 años en adelante'
]

skills = [
    'Aprendizaje rapido',
    'Proactivo',
    'Disciplinado',
    'Pensador lógico',
    'Solucionador de problemas'
]

def random_skills_(list_: list, n):
    if n == 1:
        return random.choice(list_)
    choice = random.choice(list_)
    list_.remove(choice)
    result = random_skills_(list_, n - 1)
    return result + ', ' + choice

def random_skills():
    nro_skills = random.randint(1, len(skills))
    rand_skills = random_skills_(skills[:], nro_skills)
    return rand_skills

for i in range(0, 50):
    db.add(Developer(
        first_name=FAKER.first_name(),
        last_name=FAKER.last_name(),
        phone=FAKER.phone_number(),
        experience=random.choice(years_exp),
        skills=random_skills(),
        mail=FAKER.email(),
        password=FAKER.password(),
        fk_role=1
    ))
db.commit()

print('Default insertions done!')
