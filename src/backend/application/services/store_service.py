from application.mappers.to_dto.DTOStoreMapper import DTORichStoreMapper, DTOStoreMapper
from domain.interfaces.storeInterface import StoreInterface
from domain.valueObjects.storeName import StoreName


class StoreService:
    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def get_all_stores(self):
        stores = self.store_repository.get_all_stores()
        return [DTOStoreMapper.to_store_response_dto(store) for store in stores]

    def search_stores_by_name(self, name):
        stores = self.store_repository.search_stores_by_name(StoreName(name))
        return [DTOStoreMapper.to_store_response_dto(store) for store in stores]

    def get_enriched_stores(self, name):
        stores = self.store_repository.get_enriched_stores(StoreName(name))
        return [DTORichStoreMapper.to_rich_store_response_dto(store) for store in stores]
