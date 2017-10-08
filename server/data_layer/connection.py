from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine


class DataBase:
    engine = None
    SessionMaker = None

    @staticmethod
    def get_session():
        return DataBase.SessionMaker()

    @staticmethod
    def set_engine(connection_string):
        DataBase.engine = create_engine(connection_string, connect_args={'check_same_thread': False})
        DataBase.SessionMaker = sessionmaker(bind=DataBase.engine, expire_on_commit=False)

    @staticmethod
    @contextmanager
    def transaction():
        """Provide a transactional scope around a series of operations."""
        session = DataBase.SessionMaker()
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()
