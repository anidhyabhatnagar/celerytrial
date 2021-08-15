from configparser import ConfigParser
from pymongo import MongoClient


class DBConnection:
    def __init__(self, config_file):
        config = ConfigParser()
        config.read(config_file)
        self.host = config.get('DATABASE', 'host')
        self.port = config.get('DATABASE', 'port')
        self.db_name = config.get('DATABASE', 'database')
        self.username = config.get('DATABASE', 'username')
        self.password = config.get('DATABASE', 'password')
        self.db = None
        self.client = None

    def get_connection(self):
        if self.client is None:
            self.client = MongoClient('mongodb://%s:%s/%s' % (self.host, self.port, self.db_name))
        return self.client

    def get_db(self):
        if self.client is None:
            self.get_connection()
        if self.db is None:
            self.db = self.client[self.db_name]
        return self.db

    def close_db(self):
        if self.client is not None:
            self.client.close()
            self.client = None
            self.db = None
        return True
