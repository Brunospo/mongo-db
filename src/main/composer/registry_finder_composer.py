from src.models. repository.orders_repository import OrderRepository
from src.models. connection. connection_handler import db_connection_handler
from src.use_cases. registry_finder import RegistryFinder

def registry_finder_composer():
    conn = db_connection_handler.get_connection()
    model = OrderRepository(conn)
    use_case = RegistryFinder(model)
    return use_case
