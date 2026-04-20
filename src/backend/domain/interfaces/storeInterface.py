from abc import ABC, abstractmethod
from typing import List

from domain.aggregates.store import RichStore, Store
from domain.valueObjects.storeName import StoreName


class StoreInterface(ABC):
    @abstractmethod
    def get_all_stores(self) -> List[Store]:
        """Returns a list of all stores."""
        ...

    @abstractmethod
    def search_stores_by_name(self, name: StoreName) -> List[Store]:
        """Returns a list of stores that match the given names."""
        ...

    @abstractmethod
    def get_enriched_stores_by_names(self, names: List[StoreName]) -> List[RichStore]:
        """Returns enriched stores matching the provided store names in request order."""
        ...
