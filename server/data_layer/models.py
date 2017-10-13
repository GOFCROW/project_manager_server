import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Developer(Base):
    __tablename__ = 'developer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    experience = Column(String(255), nullable=False)
    skills = Column(String(255), nullable=False)
    mail = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    fk_role = Column(Integer, ForeignKey('role_dev.id'), primary_key=True)
    enabled = Column(Boolean, nullable=False, default=True)
    projects = relationship('Project')


class ProjectDeveloper(Base):
    __tablename__ = 'project_developer'
    fk_proj = Column(Integer, ForeignKey('developer.id'), primary_key=True)
    fk_dev = Column(Integer, ForeignKey('project.id'), primary_key=True)
    hours_worked = Column(Integer, nullable=False)

class Project(Base):
      __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    estimated_hours = Column(Integer, nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)
    timestamp_created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    timestamp_modif = Column(DateTime, nullable=False)


class RoleDev(Base):
    __tablename__ = 'role_dev'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
