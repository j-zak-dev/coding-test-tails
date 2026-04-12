import pytest
from app.dependencies import get_store_repository
from application.services.store_service import StoreService

mock_stores = [
    {"name": "Mock_Store_1", "postcode": "AA1 1AA"},
    {"name": "Mock_Store_2", "postcode": "BB1 1BB"},
    {"name": "Mock_Store_3", "postcode": "CC1 1CC"},
]


@pytest.fixture
def store_service():
    store_repository = get_store_repository()
    return StoreService(store_repository)


def test_get_all_stores(store_service):
    stores = store_service.get_all_stores()
    assert isinstance(stores, list)
    assert len(stores) > 0
