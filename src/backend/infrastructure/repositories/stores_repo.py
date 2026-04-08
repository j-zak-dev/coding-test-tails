import json
from pathlib import Path

import infrastructure.services.mappers.mappers as mappers
from domain.interfaces.storeInterface import StoreInterface


class StoresRepo(StoreInterface):
    def __init__(self, mocky=False, data=None):
        if not mocky:
            data_path = Path(__file__).resolve().parents[1] / "data" / "stores.json"
            with data_path.open("r", encoding="utf-8") as file:
                self.data = json.load(file)
        else:
            self.data = data

    def get_all_stores(self):
        all_stores = [mappers.map_store_to_domain(store) for store in self.data]
        print(all_stores)
        return all_stores

    def search_stores_by_name(self, name):
        filtered_stores = [
            store for store in self.get_all_stores() if store._name.value == name.value
        ]
        return [mappers.map_store_to_domain(store) for store in filtered_stores]

    def search_store_by_postcode(self, postcode):
        filtered_stores = [
            store for store in self.get_all_stores() if store._postcode.value == postcode.value
        ]
        return [mappers.map_store_to_domain(store) for store in filtered_stores]
