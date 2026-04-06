from abc import ABC, abstractmethod
from typing import List

from backend.domain.aggregates.store import Store
from backend.domain.valueObjects.postcode import Postcode
from backend.domain.valueObjects.storeName import StoreName


class StoreInterface(ABC):
    @abstractmethod
    def get_all_stores(self) -> List[Store]:
        """Returns a list of all stores."""
        ...

    @abstractmethod
    def search_stores_by_name(self, name: StoreName) -> List[Store]:
        """Returns a list of stores that match the given namesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss."""
        ...

    @abstractmethod
    def search_store_by_postcode(self, postcode: Postcode) -> List[Store]:
        """Returns a list of stores that match the given postcode."""
        ...
