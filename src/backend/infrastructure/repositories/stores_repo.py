import json
from pathlib import Path

import infrastructure.services.mappers.mappers as mappers
from domain.interfaces.storeInterface import StoreInterface
from infrastructure.services.clients.postcodes_io_client import get_lat_and_long_from_postcode


class StoresRepo(StoreInterface):
    def __init__(self, mocky=False, data=None):
        if not mocky:
            data_path = Path(__file__).resolve().parents[1] / "data" / "stores.json"
            with data_path.open("r", encoding="utf-8") as file:
                self.data = json.load(file)
        else:
            self.data = data

    def get_all_stores(self):
        for store in self.data:
            if "latAndLong" not in store:
                store["latAndLong"] = get_lat_and_long_from_postcode(store["postcode"])

        all_stores = [mappers.map_store_to_domain(store) for store in self.data]
        return all_stores

    def search_stores_by_name(self, name):
        filtered_stores = [
            store for store in self.get_all_stores() if store._name.__value__() == name
        ]
        return filtered_stores

    def search_store_by_postcode(self, postcode):
        filtered_stores = [
            store for store in self.get_all_stores() if store._postcode.__value__() == postcode
        ]
        return filtered_stores
