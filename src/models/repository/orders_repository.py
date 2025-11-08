from pymongo.database import Database
from bson.objectid import ObjectId
from .interfaces.orders_repository import OrderRepositoryInterface

class OrderRepository(OrderRepositoryInterface):
    def __init__(self, db_connection: Database) -> None:
        self.__collection_name = 'orders'
        self.__db_connection = db_connection
    
    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one(doc_filter)
        return data
    
    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter, 
            {"id": 0, "cupom": 0} # opçoes de retorno
            )
        return data
    
    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"adress": {"$exists": True}})
        return data
    
    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)})
        return data
    
    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId("507f1f77bcf86cd799439011")}, #filtros
            {"$set": {"itens.pizza.quantidade": 30}} #edição
        )    
    
    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            {"itens.refrigerante": {"$exists": True}}, #filtros
            {"$set": {"itens.refrigerante.quantidade": 100}} #edição
        )
    
    def edit_registry_with_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId("507f1f77bcf86cd799439011")}, #filtros
            {"$inc": {"itens.pizza.quantidade": 50}} #edição
        )
    
    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one(
            {"_id": ObjectId("507f1f77bcf86cd799439011")}
        )
    
    def delete_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(
            {"itens.refrigerante": {"$exists": True}}
        )
