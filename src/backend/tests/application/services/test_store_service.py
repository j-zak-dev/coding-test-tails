import pytest
from application.services.store_service import StoreService
from infrastructure.repositories.stores_repo import StoresRepo
from infrastructure.services.clients.mocky_postcode_io_client import get_mocky_postcode_io_response

mock_stores = [
    {"name": "Mock_Store_1", "postcode": "AA1 1AA"},
    {"name": "Mock_Store_2", "postcode": "BB1 1BB"},
    {"name": "Mock_Store_3", "postcode": "CC1 1CC"},
]


@pytest.fixture
def store_service():
    store_repository = StoresRepo(get_coords_fn=get_mocky_postcode_io_response, data=mock_stores)
    return StoreService(store_repository)


def test_get_all_stores(store_service):
    stores = store_service.get_all_stores()
    assert isinstance(stores, list)
    assert len(stores) > 0


def test_search_stores_by_name(store_service):
    stores = store_service.search_stores_by_name("Mock_Store_2")
    assert isinstance(stores, list)
    assert len(stores) == 1
    assert stores[0].name == "Mock_Store_2"
