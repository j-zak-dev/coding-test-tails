from application.mappers.to_dto.DTOStoreMapper import DTOStoreMapper
from domain.interfaces.storeInterface import StoreInterface


class StoreService:
    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def get_all_stores(self):
        stores = self.store_repository.get_all_stores()
        return [DTOStoreMapper.to_store_response_dto(store) for store in stores]

    def search_stores_by_name(self, name):
        stores = self.store_repository.search_stores_by_name(name)
        return [DTOStoreMapper.to_store_response_dto(store) for store in stores]

    def search_store_by_postcode(self, postcode):
        stores = self.store_repository.search_store_by_postcode(postcode)
        return [DTOStoreMapper.to_store_response_dto(store) for store in stores]
