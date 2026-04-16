from domain.valueObjects.latAndLong import LatAndLong
from domain.valueObjects.postcode import Postcode
from domain.valueObjects.storeId import StoreID
from domain.valueObjects.storeName import StoreName


class Store:
    def __init__(self, id: StoreID, name: StoreName, postcode: Postcode):
        self._id = id if isinstance(id, StoreID) else StoreID(id)
        self._name = name if isinstance(name, StoreName) else StoreName(name)
        self._postcode = postcode if isinstance(postcode, Postcode) else Postcode(postcode)


class RichStore(Store):
    def __init__(self, id: StoreID, name: StoreName, postcode: Postcode, latAndLong: LatAndLong):
        super().__init__(id, name, postcode)
        self._latAndLong = (
            latAndLong
            if isinstance(latAndLong, LatAndLong)
            else LatAndLong(latAndLong[0], latAndLong[1])
        )
