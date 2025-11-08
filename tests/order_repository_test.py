import sys

from bson import ObjectId
sys.path.append('../')

from src.models.repository.orders_repository import OrderRepository

class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_atributtes = {}
        self.find_attributes = {}
        self.update_attributes = {}
    
    def insert_one(self, input_data: any):
        self.insert_one_atributtes['dict'] = input_data

    def find(self, *args):
        self.find_attributes['args'] = args
    
    def update_one(self, *args):
        self.update_attributes['args'] = args

class DbConnectiomock:
    def __init__(self, collection) -> None:
        self.get_collection_attributes = {}
        self.collection = collection
    
    def get_collection(self, collection_name):
        self.get_collection_attributes['name'] = collection_name
        return self.collection

def test_insert_document():
    collection = CollectionMock()
    db_connection = DbConnectiomock(collection)
    repo = OrderRepository(db_connection)

    doc = {"some": "thing"}
    repo.insert_document(doc)

    assert collection.insert_one_atributtes['dict'] == doc

def test_select_many_with_properties():
    collection = CollectionMock()
    db_connection = DbConnectiomock(collection)
    repo = OrderRepository(db_connection)

    doc = {"some": "thing"}
    repo.select_many_with_properties(doc)

    assert collection.find_attributes['args'][0] == doc
    assert collection.find_attributes['args'][1] == {"id": 0, "cupom": 0}

def test_edit_registry():
    collection = CollectionMock()
    db_connection = DbConnectiomock(collection)
    repo = OrderRepository(db_connection)
    repo.edit_registry()

    assert collection.update_attributes['args'][0] == {'_id': ObjectId('507f1f77bcf86cd799439011')}
    assert collection.update_attributes['args'][1] == {'$set': {'itens.pizza.quantidade': 30}}
