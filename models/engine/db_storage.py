''' storage db mysql manager
'''

from models.city import City
from models.state import State
from os import getenv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

CLASS_LIST = [State, City]


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        uri = 'mysql+mysqldb://{}:{}@{}/{}'
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_password = getenv("HBNB_MYSQL_PWD")
        mysql_host = 'localhost'
        mysql_db = getenv('HBNB_MYSQL_DB')

        DBStorage.__engine = create_engine(uri.format(
            mysql_user, mysql_password, mysql_host, mysql_db), pool_pre_ping=True)

        DBStorage.__session = sessionmaker()()

    def all_cls_to_dict(self, cls):
        dict_info = {}
        for row in self.__session.query(cls).all():
            key = "{}.{}".format(cls.__name__, row.id)
            dict_info.update({key: row})
        return dict_info

    def all(self, cls=None):
        '''get all of cls'''

        if cls:
            return self.all_cls_to_dict(cls)
        dict_info = {}
        if not cls:
            for class_name in CLASS_LIST:
                dict_info.update(self.all_cls_to_dict(class_name))
        return dict_info

    def new(self, obj):
        '''add new element'''
        self.__session.add(obj)
        self.save()

    def save(self):
        '''save transaction'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete object '''
        self.__session.delete(obj)

    def reload(self):
        '''recreate model'''
        from models.base_model import Base
        from models.state import State
        from models.city import City
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
