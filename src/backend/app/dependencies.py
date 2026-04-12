from domain.interfaces.storeInterface import StoreInterface
from infrastructure.storeRepository import StoreRepository


def main():
    store_repository: StoreInterface = StoreRepository()
    return store_repository
