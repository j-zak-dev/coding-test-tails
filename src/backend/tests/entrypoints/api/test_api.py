import pytest
from application.services.store_service import StoreService
from dependencies import get_store_service
from entrypoints.api.main import app
from fastapi.testclient import TestClient
from infrastructure.repositories.stores_repo import StoresRepo
from infrastructure.services.clients.mocky_postcode_io_client import get_mocky_postcode_io_response

mock_stores = [
    {"name": "Mock_Store_1", "postcode": "AA1 1AA"},
    {"name": "Mock_Store_2", "postcode": "BB1 1BB"},
    {"name": "Mock_Store_3", "postcode": "CC1 1CC"},
]


@pytest.fixture
def client():
    def override_get_store_service() -> StoreService:
        store_repository = StoresRepo(
            get_coords_fn=get_mocky_postcode_io_response,
            data=mock_stores,
        )
        return StoreService(store_repository)

    app.dependency_overrides[get_store_service] = override_get_store_service
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def test_get_all_stores_endpoint(client):
    response = client.get("/stores")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3


def test_search_stores_by_name_endpoint(client):
    response = client.get("/stores/search_by_name/Mock_Store_2")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Mock_Store_2"
    assert data[0]["postcode"] == "BB1 1BB"


def test_search_store_by_postcode_endpoint(client):
    response = client.get("/stores/search_by_postcode/CC1 1CC")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Mock_Store_3"
    assert data[0]["postcode"] == "CC1 1CC"
