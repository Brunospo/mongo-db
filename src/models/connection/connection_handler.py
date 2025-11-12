from pymongo import MongoClient
from src.configs.mongo_connection_infos import USERNAME, PASSWORD, PORT, HOST, DATABASE_NAME

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/?authSource=admin'
        self.__database_name = DATABASE_NAME
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
    
    def get_connection(self):
        return self.__db_connection

db_connection_handler = DBConnectionHandler()
