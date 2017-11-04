# import hashlib
import sqlite3
import random as rand

from configparser import ConfigParser
from faker import Faker

from server import DataBase
from server.data_layer.models import (
    Assignment,
    Developer,
    Project,
    Base
)
# PARAMS

NUMBER_DEVS = 50
NUMBER_PROJS = 8

ROLES = [
    'Gestor de proyecto',
    'Programador',
    'Diseñador',
    'Analista',
    'Tester'
]

EXPERIENCE = [
    'menos de 2 año',
    'de 2 - 4 años',
    'de 4 - 7 años',
    'de 7 años en adelante'
]

SKILLS = [
    'Aprendizaje rapido',
    'Proactivo',
    'Disciplinado',
    'Pensador lógico',
    'Solucionador de problemas'
]

# SCRIPT
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


def random_skills_(list_: list, n):
    if n == 1:
        return rand.choice(list_)
    choice = rand.choice(list_)
    list_.remove(choice)
    result = random_skills_(list_, n - 1)
    return result + ', ' + choice

def random_skills():
    nro_skills = rand.randint(1, len(SKILLS))
    rand_skills = random_skills_(SKILLS[:], nro_skills)
    return rand_skills

FAKER = Faker()
for i in range(1, NUMBER_DEVS + 1):
    db.add(Developer(
        first_name=FAKER.first_name(),
        last_name=FAKER.last_name(),
        phone_number=FAKER.phone_number(),
        experience=rand.choice(EXPERIENCE),
        skills=random_skills(),
        email=FAKER.email(),
        password=FAKER.password(),
    ))
db.commit()

for i in range(1, NUMBER_PROJS + 1):
    p = Project(
        name='proyecto ' + FAKER.city(),
        description=FAKER.sentence(),
        estimated_hours=rand.randint(40, 700),
    )

    taken_devs = list()

    for i in range(0, rand.randint(2, 10)):
        fk_dev = rand.randint(1, NUMBER_DEVS)
        while fk_dev in taken_devs:
            fk_dev = rand.randint(1, NUMBER_DEVS)
        taken_devs.append(fk_dev)

        p.assignments.append(Assignment(
            hours_worked=rand.randint(0, 690),
            fk_dev=fk_dev,
        ))
    db.add(p)
db.commit()

print('Default insertions done!')
