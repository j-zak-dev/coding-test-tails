from application.dtos.store_response_dto import RichStoreResponseDTO, StoreResponseDTO
from domain.aggregates.store import RichStore, Store


class DTOStoreMapper:
    @staticmethod
    def to_store_response_dto(store: Store) -> StoreResponseDTO:
        return StoreResponseDTO(
            name=store._name.value(),
            postcode=store._postcode.value(),
        )


class DTORichStoreMapper:
    @staticmethod
    def to_rich_store_response_dto(store: RichStore) -> RichStoreResponseDTO:
        return RichStoreResponseDTO(
            name=store._name.value(),
            postcode=store._postcode.value(),
            latAndLong=(store._latAndLong.latitude, store._latAndLong.longitude),
        )
