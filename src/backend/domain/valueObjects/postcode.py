from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Postcode:
    postcode: str

    def __post_init__(self):
        """Validates the postcode."""
        if not self.postcode:
            raise ValueError("Postcode cannot be empty.")
        if len(self.postcode) > 8:
            raise ValueError("Postcode cannot exceed 8 characters.")

    def __value__(self) -> str:
        """Returns the postcode."""
        return self.postcode

    ## TO DO: Rename the method that gets the value, consider using a magic method.
