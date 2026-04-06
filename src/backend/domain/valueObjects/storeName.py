from dataclasses import dataclass

@dataclass(frozen=True)
class StoreName:
    name: str
    
    def __post_init__(self):
        """Validates the store name."""
        if not self.name:
            raise ValueError("Store name cannot be empty.")
        if len(self.name) > 50:
            raise ValueError("Store name cannot exceed 50 characters.")
        
    def name(self) -> str:
        """Returns the name of the store."""
        return self.name