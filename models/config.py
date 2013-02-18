__author__ = 'Abraham Aondowase Yusuf <bb6xt@yahoo.com>'

import copy
import json
from PySide import QtCore

class DBConnection(object):
    __conn = None

    def __init__(self, name, server='localhost', port=27017, user='', passwd='', dbnames=[]):
        self.__conn = (name, server, port, user, passwd, self.parse_db_names(dbnames))
        # save using either qsettings or db

    @property
    def name(self):
        return self.__conn[0]

    @property
    def server(self):
        return self.__conn[1]

    @property
    def port(self):
        return self.__conn[2]

    @property
    def user(self):
        return self.__conn[3]

    @property
    def passwd(self):
        return self.__conn[4]

    @property
    def dbnames(self):
        return self.__conn[5]

    def to_dict(self):
        _params = {
            'name': self.name, 'server': self.server, 'port': self.port,
            'user': self.user, 'passwd': self.passwd, 'dbnames': self.dbnames
        }

        return _params

    @classmethod
    def parse_db_names(cls, str_db_list):
        # todo check each dbname to prevent JavaScript Injection (a la SQL injection)
        dbnames = copy.deepcopy(str_db_list)
        return  dbnames # now you know why I have that to do just there


class StorageMeta(type):
    # a metaclass for a singleton object
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            StorageMeta._instance = type.__new__(cls, *args, **kwargs)

        return StorageMeta._instance

class ConnectionStore(object):
    __metaclass__ = StorageMeta

    @property
    def all(self):
        # ConnectionStore = {'con1_name': con1_as_dict, 'con2_name': con2_as_dict, etc}
        store = QtCore.QSettings().value('ConnectionStore', json.dumps({}))
        rt = []

        for value in json.loads(store).values():
            rt.append(DBConnection(**value))

        return tuple(rt)

    @all.setter
    def all(self, value):
        pass # don't set anything

    @property
    def names(self):
        return tuple([i.name for i in self.all])

    @names.setter
    def names(self, value):
        pass # don't set anything

    # todo: need to allow a way of storing connections in a namespace eg QtCore.QSettings().setValue('connections', {'conn_1': conn1_json, 'conn2': conn2_json}
    # this way we can have a ConnectionStore.get_all() method. However, retrieving a single conn will b more involved.
    # why am I doing this? Don't want to use SQLite or any db for persisting connection infos

    def pull(self, connection_name):
        # retrieve the connection and create a DBConnection instance of the connection and return
        for i in self.all:
            if i.name == connection_name:
                return i

        raise Exception('Connection Not Found!')

    def push(self, db_connection):
        if not isinstance(db_connection, DBConnection):
            raise Exception('db_connection must be an instance of {}'.format(DBConnection.__name__))

        # this will override any previous setting with the same name
        settings = QtCore.QSettings()

        store = json.loads(settings.value('ConnectionStore', json.dumps({})))
        store.update({db_connection.name: db_connection.to_dict()})
        settings.setValue('ConnectionStore', json.dumps(store))

    @classmethod
    def remove(cls, connection_name):
        settings = QtCore.QSettings()

        store = json.loads(settings.value('ConnectionStore', json.dumps({})))
        if connection_name in store.keys():
            del store[connection_name]

        settings.setValue('ConnectionStore', json.dumps(store))