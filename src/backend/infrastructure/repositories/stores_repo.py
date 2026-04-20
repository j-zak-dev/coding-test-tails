import uuid

from domain.interfaces.storeInterface import StoreInterface
from domain.valueObjects.storeName import StoreName
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
            stores_for_mapping.append(store_copy)

        all_stores = [mappers.map_store_to_domain_store(store) for store in stores_for_mapping]
        return all_stores

    def search_stores_by_name(self, name: StoreName):
        filtered_stores = [
            store
            for store in self.get_all_stores()
            if name.value().lower() in store._name.value().lower()
            or name.value().lower() in store._postcode.value().lower()
        ]
        return sorted(filtered_stores, key=lambda store: store._postcode.value().casefold())

    def get_enriched_stores_by_names(self, names: list[StoreName]):
        names_lookup = [name.value().lower() for name in names]
        if not names_lookup:
            return []

        all_stores = self.get_all_stores()
        stores_by_name = {store._name.value().lower(): store for store in all_stores}

        enriched_stores = []
        seen = set()
        for store_name in names_lookup:
            if store_name in seen:
                continue
            seen.add(store_name)

            store = stores_by_name.get(store_name)
            if store is None:
                continue

            latAndLong = self.get_coords_fn(store._postcode.value())
            enriched_store = mappers.map_store_to_domain_rich_store(
                {
                    "id": store._id.value(),
                    "name": store._name.value(),
                    "postcode": store._postcode.value(),
                    "latAndLong": latAndLong,
                }
            )
            enriched_stores.append(enriched_store)

        return enriched_stores

    def get_enriched_stores(self, name: StoreName):
        # Backward-compatible helper for older callers.
        enriched_stores = []
        for store in self.search_stores_by_name(name):
            if (
                name.value().lower() in store._name.value().lower()
                or name.value().lower() in store._postcode.value().lower()
            ):
                latAndLong = self.get_coords_fn(store._postcode.value())
                enriched_store = mappers.map_store_to_domain_rich_store(
                    {
                        "id": store._id.value(),
                        "name": store._name.value(),
                        "postcode": store._postcode.value(),
                        "latAndLong": latAndLong,
                    }
                )
                enriched_stores.append(enriched_store)
        return enriched_stores
