import sys
sys.path.append('../')

from src.use_cases.registry_updater import RegistryUpdater
from src.main.http_types.http_request import HttpRequest

class MockRepository():    
    def edit_registry(self, order_id: str, update_field: dict) -> None:
        pass

def test_registry_updater():
    repo = MockRepository()
    registry_updater = RegistryUpdater(repo)

    http_request = HttpRequest(
        params={'order_id': '507f1f77bcf86cd799439011'}, 
        body={
        "data": {            
            "name": "Jhon Doe",
            "address": "Some Address, number 123",
            "cupom": False            
        }
    })

    response = registry_updater.update(http_request)

    assert response.status_code == 200
    assert response.body['data']['count'] == 1
    assert response.body['data']['type'] == "Order"
    assert response.body['data']['order_id'] == '507f1f77bcf86cd799439011'

def test_registry_finder_error():
    repo = MockRepository()
    registry_updater = RegistryUpdater(repo)

    http_request = HttpRequest(
        params={'order_id': '507f1f77bcf86cd799439011'}, 
        body={
        "data": {            
            "name": 1,
            "address": "Some Address, number 123",
            "cupom": False            
        }
    })

    response = registry_updater.update(http_request)

    assert response.status_code == 422
    assert response.body['errors'][0]['title'] == 'UnprocessableEntity'
