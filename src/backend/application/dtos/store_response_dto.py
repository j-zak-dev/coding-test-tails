from pydantic import BaseModel, Field


class StoreResponseDTO:
    def __init__(self, name: str, postcode: str):
        self.name = name
        self.postcode = postcode


class RichStoreResponseDTO(StoreResponseDTO):
    def __init__(self, name: str, postcode: str, latAndLong: tuple):
        super().__init__(name, postcode)
        self.latAndLong = latAndLong


class EnrichedStoresByNamesRequestDTO(BaseModel):
    storeNames: list[str] = Field(default_factory=list)
