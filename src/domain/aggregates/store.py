from domain.valueObjects.latandLong import LatAndLong
from domain.valueObjects.storeId import StoreID
from domain.valueObjects.storeName import StoreName
from domain.valueObjects.postcode import Postcode

class StoreObject:
    def __init__(self,id: StoreID, name: StoreName, postcode: Postcode, latAndLong: LatAndLong):
        self._id = id
        self._name = name
        self._postcode = postcode
        self._latAndLong = latAndLong
        