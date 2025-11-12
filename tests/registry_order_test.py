import sys
sys.path.append('../')

from src.use_cases.registry_order import RegistryOrder
from src.main.http_types.http_request import HttpRequest

class MockRepository():
    def __init__(self) -> None:
        self.insert_document_att = {}
    
    def insert_document(self, document: dict) -> None:
        self.insert_document_att['document'] = document

class MockRepositoryError():
    def insert_document(self, document: dict) -> None:
        raise Exception('Erro aqui')

def test_registry_order():
    repo = MockRepository()
    registry_order = RegistryOrder(repo)

    http_request = HttpRequest(body={
        "data": {
            "name": "Jhon",
            "address": "Main Street, Apt 4B",
            "cupom": False,
            "items": [
                {"item": "Refrigerante", "quantidade": 2},
                {"item": "Pizza", "quantidade": 3}
            ]
        }
    })

    response = registry_order.registry(http_request)
    
    assert "name" in repo.insert_document_att["document"]
    assert "address" in repo.insert_document_att["document"]
    assert "created_at" in repo.insert_document_att["document"]

    assert response.status_code == 201
    assert response.body['data']['count'] == 1
    assert response.body['data']['type'] == "Order"

def test_registry_order_error():
    repo = MockRepositoryError()
    registry_order = RegistryOrder(repo)

    http_request = HttpRequest(body={
        "data": {
            "name": "Jhon",
            "address": "Main Street, Apt 4B",
            "cupom": False,
            "items": [
                {"item": "Refrigerante", "quantidade": 2},
                {"item": "Pizza", "quantidade": 3}
            ]
        }
    })

    response = registry_order.registry(http_request)      
    
    assert response.status_code == 400
    assert response.body['error'] == 'Erro aqui'
