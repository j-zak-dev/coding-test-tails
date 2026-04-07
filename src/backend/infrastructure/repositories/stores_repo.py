import json
from pathlib import Path

import infrastructure.services.mappers.mappers as mappers
from domain.interfaces.storeInterface import StoreInterface


class StoresRepo(StoreInterface):
    def __init__(self, max=None):
        self.max = max

    def get_all_stores(self):
        data_path = Path(__file__).resolve().parents[1] / "data" / "stores.json"

        with data_path.open("r", encoding="utf-8") as file:
            stores_from_data = json.load(file)

        return [mappers.map_store_to_domain(store) for store in stores_from_data[: self.max]]

    def search_stores_by_name(self, name):
        filtered_stores = [
            store for store in self.get_all_stores() if store._name.value == name.value
        ]
        return [mappers.map_store_to_domain(store) for store in filtered_stores[: self.max]]

    def search_store_by_postcode(self, postcode):
        filtered_stores = [
            store for store in self.get_all_stores() if store._postcode.value == postcode.value
        ]
        return [mappers.map_store_to_domain(store) for store in filtered_stores[: self.max]]
