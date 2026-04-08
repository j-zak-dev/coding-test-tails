from infrastructure.repositories.stores_repo import StoresRepo


def test_get_all_stores_uses_mock_data():
    """Robust test to check if all stores are returned by the repo, and whether coordinates are assigned"""
    mock_stores = [
        {"name": "Mock_Store_1", "postcode": "AA1 1AA"},
        {"name": "Mock_Store_2", "postcode": "BB1 1BB"},
        {"name": "Mock_Store_3", "postcode": "CC1 1CC"},
    ]

    repo = StoresRepo(mocky=True, data=mock_stores)
    stores = repo.get_all_stores()

    for index, store in enumerate(stores):
        assert store._name.name == f"Mock_Store_{index + 1}"
        assert store._postcode.postcode == mock_stores[index]["postcode"]
        assert hasattr(store, "_latAndLong")
    assert len(stores) == 3
