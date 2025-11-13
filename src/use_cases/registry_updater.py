from src.models.repository.interfaces.orders_repository import OrderRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.error_handler import handle_errors
from src.validators.registry_updater_validator import registry_updater_validator

class RegistryUpdater:
    def __init__(self, orders_repository: OrderRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def update(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.params['order_id']
            body = http_request.body

            self.__validate_body(body)
            self.__update_order(order_id, body)

            return self.__format_response(order_id)
        except Exception as exception:
            return handle_errors(exception)
    
    def __validate_body(self, body:dict) -> None:
        registry_updater_validator(body)
        
    def __update_order(self, order_id: str, body: dict) -> None:
        update_field = body["data"]
        self.__orders_repository.edit_registry(order_id, update_field)

    def __format_response(self, order_id: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "Order",
                    "count": 1,
                    "order_id": order_id
                }
            },
            status_code=200
        )
      