from typing import List


class StoreResponseDTO:
    def __init__(self, name: str, postcode: str, latAndLong: List[float]):
        self.name = name
        self.postcode = postcode
        self.latAndLong = latAndLong
