import sys
sys.path.append('../')

from src.use_cases.registry_finder import RegistryFinder
from src.main.http_types.http_request import HttpRequest

order_mock = {
            '_id': '507f1f77bcf86cd799439011',
            "name": "joaozinho",
            "address": "rua do limao",
            "cupom": False,
            "items": [
                {"item": "Refrigerante", "quantidade": 2},
                {"item": "pizza", "quantidade": 3}
            ]
        }

class MockRepository():    
    def select_by_object_id(self, order_id: str) -> None:
        return order_mock

class MockRepositoryError():
    def select_by_object_id(self, order_id: str) -> None:
        return None

def test_registry_finder():
    repo = MockRepository()
    registry_finder = RegistryFinder(repo)

    http_request = HttpRequest(params={'order_id': '507f1f77bcf86cd799439011'})

    response = registry_finder.find(http_request)

    assert response.status_code == 200
    assert response.body['data']['count'] == 1
    assert response.body['data']['type'] == "Order"
    assert response.body['data']['attributes'] == order_mock

def test_registry_finder_error():
    repo = MockRepositoryError()
    registry_finder = RegistryFinder(repo)

    http_request = HttpRequest(params={'order_id': '507f1f77bcf86cd799439011'})

    response = registry_finder.find(http_request)

    assert response.status_code == 404
    assert response.body['errors'][0]['title'] == 'NotFound'
