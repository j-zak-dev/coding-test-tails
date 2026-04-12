import uuid

from domain.interfaces.storeInterface import StoreInterface
from infrastructure.services.mappers import mappers


class StoresRepo(StoreInterface):
    def __init__(self, data=None, get_coords_fn=None):
        self.get_coords_fn = get_coords_fn
        self.data = data or []

    def get_all_stores(self):
        stores_for_mapping = []
        for store in self.data:
            store_copy = dict(store)
            store_copy["id"] = uuid.uuid4()
            store_copy["latAndLong"] = self.get_coords_fn(store_copy["postcode"])
            stores_for_mapping.append(store_copy)

        all_stores = [mappers.map_store_to_domain(store) for store in stores_for_mapping]
        return all_stores

    def search_stores_by_name(self, name):
        filtered_stores = [store for store in self.get_all_stores() if store._name.value() == name]
        return filtered_stores

    def search_store_by_postcode(self, postcode):
        filtered_stores = [
            store for store in self.get_all_stores() if store._postcode.value() == postcode
        ]
        return filtered_stores
