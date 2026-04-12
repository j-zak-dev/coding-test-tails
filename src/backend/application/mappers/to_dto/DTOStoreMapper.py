from application.dtos.store_response_dto import StoreResponseDTO
from domain.aggregates.store import Store


class DTOStoreMapper:
    @staticmethod
    def to_store_response_dto(store: Store) -> StoreResponseDTO:
        return StoreResponseDTO(
            name=store._name.value(),
            postcode=store._postcode.value(),
            latAndLong=store._latAndLong.values(),
        )
