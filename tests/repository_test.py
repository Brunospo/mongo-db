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
