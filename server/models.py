from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Developer(Base):
    __tablename__ = 'developer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    mail = Column(String(100), nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)


class ProjectDeveloper(Base):
    __tablename__ = 'project_developer'

    dev_id = Column(Integer, ForeignKey('developer.id'), primary_key=True)
    pro_id = Column(Integer, ForeignKey('project.id'), primary_key=True)


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)
