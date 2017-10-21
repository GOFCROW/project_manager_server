import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from .serializable import Serializable

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Developer(Serializable, Base):
    __tablename__ = 'developer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(20), nullable=False)
    experience = Column(String(255), nullable=False)
    skills = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)

    assignments = relationship('Assignment')


class Assignment(Serializable, Base):
    __tablename__ = 'assignment'
    fk_dev = Column(Integer, ForeignKey('developer.id'), primary_key=True)
    fk_proj = Column(Integer, ForeignKey('project.id'), primary_key=True)
    fk_role = Column(Integer, ForeignKey('role_dev.id'))
    hours_worked = Column(Integer, nullable=False)

    developer = relationship('Developer')
    project = relationship('Project')
    role = relationship('RoleDev')


class Project(Serializable, Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    estimated_hours = Column(Integer, nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)

    assignments = relationship('Assignment')


class RoleDev(Serializable, Base):
    __tablename__ = 'role_dev'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
