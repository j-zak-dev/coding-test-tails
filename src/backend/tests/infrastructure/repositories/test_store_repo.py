from infrastructure.repositories.stores_repo import StoresRepo
from infrastructure.services.clients.mocky_postcode_io_client import get_mocky_postcode_io_response
from infrastructure.services.clients.postcodes_io_client import get_lat_and_long_from_postcode

mock_stores = [
    {"name": "Mock_Store_1", "postcode": "AA1 1AA"},
    {"name": "Mock_Store_2", "postcode": "BB1 1BB"},
    {"name": "Mock_Store_3", "postcode": "CC1 1CC"},
]

repo = StoresRepo(get_coords_fn=get_mocky_postcode_io_response, data=mock_stores)


def test_get_all_stores_uses_mock_data():
    """Robust test to check if all stores are returned by the repo."""
    stores = repo.get_all_stores()
    for index, store in enumerate(stores):
        assert store._name.value() == f"Mock_Store_{index + 1}"
        assert store._postcode.value() == mock_stores[index]["postcode"]
        assert hasattr(store, "_latAndLong")
    assert len(stores) == 3


def test_search_stores_by_name():
    """Test to check if searching by name returns the correct store"""
    stores = repo.search_stores_by_name("Mock_Store_2")
    assert len(stores) == 1
    assert stores[0]._name.value() == "Mock_Store_2"
    assert stores[0]._postcode.value() == "BB1 1BB"


def test_search_store_by_postcode():
    """Test to check if searching by postcode returns the correct store"""
    stores = repo.search_store_by_postcode("CC1 1CC")
    assert len(stores) == 1
    assert stores[0]._name.value() == "Mock_Store_3"
    assert stores[0]._postcode.value() == "CC1 1CC"


def test_postcodes_io_integration():
    """Test to check if the call to postcodes.io works correctly."""
    mock_stores = [
        {"name": "Mock_Store_1", "postcode": "SO50 5GD"},
        {"name": "Mock_Store_2", "postcode": "CH70 8DA"},
    ]

    repo = StoresRepo(data=mock_stores, get_coords_fn=get_lat_and_long_from_postcode)
    stores = repo.get_all_stores()

    for index, store in enumerate(stores):
        assert store._name.value() == f"Mock_Store_{index + 1}"
        assert store._postcode.value() == mock_stores[index]["postcode"]
        assert hasattr(store, "_latAndLong")
        assert store._latAndLong.values() != [
            0.0,
            0.0,
        ]  # Check that lat and long are assigned correctly
    assert len(stores) == 2
