from backend.domain.valueObjects.latAndLong import LatAndLong
from backend.domain.valueObjects.postcode import Postcode
from backend.domain.valueObjects.storeId import StoreID
from backend.domain.valueObjects.storeName import StoreName


class Store:
    def __init__(self, id: StoreID, name: StoreName, postcode: Postcode, latAndLong: LatAndLong):
        self._id = id if isinstance(id, StoreID) else StoreID(id)
        self._name = name if isinstance(name, StoreName) else StoreName(name)
        self._postcode = postcode if isinstance(postcode, Postcode) else Postcode(postcode)
        self._latAndLong = (
            latAndLong if isinstance(latAndLong, LatAndLong) else LatAndLong(latAndLong)
        )
