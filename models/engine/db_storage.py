''' storage db mysql manager
'''

from models.review import Review
from models.place import Place
from models.user import User
from models.base_model import Base
from models.city import City
from models.state import State
from os import getenv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

CLASS_LIST = [State, City, User, Place, Review]


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """ storage constructor perform connection"""
        uri = 'mysql+mysqldb://{}:{}@{}/{}'
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_password = getenv("HBNB_MYSQL_PWD")
        mysql_host = 'localhost'
        mysql_db = getenv('HBNB_MYSQL_DB')

        DBStorage.__engine = create_engine(uri.format(
            mysql_user, mysql_password, mysql_host, mysql_db), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all_cls_to_dict(self, cls):
        """objects to dict"""
        query = self.__session.query(cls).all()
        return self.list_to_dict(query, cls)

    def list_to_dict(self, list, cls):
        dict_info = {}
        for row in list:
            key = "{}.{}".format(cls.__name__, row.id)
            dict_info.update({key: row})
        return dict_info

    def all(self, cls=None):
        '''get all of cls'''

        if cls:
            return self.all_cls_to_dict(cls)
        dict_info = {}

        for class_name in CLASS_LIST:
            dict_info.update(self.all_cls_to_dict(class_name))
        return dict_info

    def by_id(self, cls):
        query = self.__session.query(cls).filter(cls["id"]).all()
        return self.list_to_dict(query)

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
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
