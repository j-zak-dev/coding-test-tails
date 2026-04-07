import json
from pathlib import Path

import infrastructure.services.mappers.mappers as mappers
from domain.interfaces.storeInterface import StoreInterface


class StoresRepo(StoreInterface):
    def get_all_stores(self):
        data_path = Path(__file__).resolve().parents[1] / "data" / "stores.json"

        with data_path.open("r", encoding="utf-8") as file:
            stores_from_data = json.load(file)

        return [mappers.map_store_to_domain(store) for store in stores_from_data]

    def search_stores_by_name(self, name):
        # Implementation to search stores by name in the database
        pass

    def search_store_by_postcode(self, postcode):
        # Implementation to search stores by postcode in the database
        pass
