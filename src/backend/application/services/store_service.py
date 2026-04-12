from domain.interfaces.storeInterface import StoreInterface


class StoreService:
    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def get_all_stores(self):
        return self.store_repository.get_all_stores()

    def search_stores_by_name(self, name):
        return self.store_repository.search_stores_by_name(name)

    def search_store_by_postcode(self, postcode):
        return self.store_repository.search_store_by_postcode(postcode)
