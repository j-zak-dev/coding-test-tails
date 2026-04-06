import uuid
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StoreID:
    storeId: uuid.UUID

    def __post_init__(self):
        """Validates the store ID."""
        if not self.storeId:
            raise ValueError("Store ID cannot be empty.")
        if len(str(self.storeId)) > 36:
            raise ValueError("Store ID cannot exceed 36 characters.")

    def id(self) -> str:
        """Returns the store ID."""
        return str(self.storeId)
