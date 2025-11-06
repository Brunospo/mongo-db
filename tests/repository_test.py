import sys
sys.path.append('../')

import pytest

from src.models.connection.connection_handler import DBConnectionHandler
from src.models.repository.orders_repository import OrderRepository

db_connection = DBConnectionHandler()
db_connection.connect_to_db()
conn = db_connection.get_connection()

@pytest.mark.skip(reason='Interação com o banco')
def test_insert_document():
    order_repository = OrderRepository(conn)
    my_doc = {"some": "thing", "value": 1}
    order_repository.insert_document(my_doc)

@pytest.mark.skip(reason='Interação com o banco')    
def test_insertlist_of_documents():
    order_repository = OrderRepository(conn)
    list_doc = [{"some": "thing", "value": 1}, {"some2": "thing2", "value": 2}]
    order_repository.insert_list_of_documents(list_doc)

@pytest.mark.skip(reason='Interação com o banco')
def test_select_many_documents():
    order_repository = OrderRepository(conn)
    doc_filter = {"cupom": True}
    response = order_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        print(doc)

@pytest.mark.skip(reason='Interação com o banco')
def test_select_one_document():
    order_repository = OrderRepository(conn)
    doc_filter = {"cupom": True}
    response = order_repository.select_one(doc_filter)
    print()
    print(response)
    for doc in response:
        print(doc)

@pytest.mark.skip(reason='Interação com o banco')
def test_select_many_with_properties():
    order_repository = OrderRepository(conn)
    doc_filter = {"cupom": True}
    response = order_repository.select_many_with_properties(doc_filter)
    print()
    for doc in response:
        print(doc)

@pytest.mark.skip(reason='Interação com o banco')
def test_if_property_exists():
    order_repository = OrderRepository(conn)
    response = order_repository.select_if_property_exists()
    print()
    for doc in response:
        print(doc)

@pytest.mark.skip(reason='Interação com o banco')
def test_select_many_documents_with_multiple_filter():
    order_repository = OrderRepository(conn)
    doc_filter = {
        "cupom": True, 
        "itens.doce": {"$exists": True}
        } #Semelhante a uma busca AND em SQL
    response = order_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)

@pytest.mark.skip(reason='Interação com o banco')
def test_select_many_documents_with_or_filter():
    order_repository = OrderRepository(conn)
    doc_filter = {
        "$or": [
            {"adress": {"$exists": True}},
            {"itens.doce.tipo": "chocolate"}
        ]
        } #Semelhante a uma busca OR em SQL
    response = order_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)

@pytest.mark.skip(reason='Interação com o banco')
def test_select_by_object_id():
    order_repository = OrderRepository(conn)
    object_id = "5740h435bn493877"
    response = order_repository.select_by_object_id(object_id)
    print()
    for doc in response:
        print(doc)

@pytest.mark.skip(reason='Interação com o banco')
def test_edit_registry():
    order_repository = OrderRepository(conn)
    order_repository.edit_registry()

@pytest.mark.skip(reason='Interação com o banco')
def test_edit_many_registries():
    order_repository = OrderRepository(conn)
    order_repository.edit_many_registries()

@pytest.mark.skip(reason='Interação com o banco')
def test_edit_registry_with_increment():
    order_repository = OrderRepository(conn)
    order_repository.edit_registry_with_increment()
    
@pytest.mark.skip(reason='Interação com o banco')
def test_delete_registry():
    order_repository = OrderRepository(conn)
    order_repository.delete_registry()

@pytest.mark.skip(reason='Interação com o banco')
def test_delete_many_registries():
    order_repository = OrderRepository(conn)
    order_repository.delete_many_registries()
