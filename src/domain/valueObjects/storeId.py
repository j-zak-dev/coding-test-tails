from dataclasses import dataclass

class StoreID:
    
    def __post_init__(self):
        """Validates the store ID."""
        if not self._id:
            raise ValueError("Store ID cannot be empty.")
        if len(self._id) > 20:
            raise ValueError("Store ID cannot exceed 20 characters.")
    
    def id(self) -> str:
        """Returns the store ID."""
        return self._id