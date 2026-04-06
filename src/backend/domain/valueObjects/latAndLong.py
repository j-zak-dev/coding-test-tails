from dataclasses import dataclass

@dataclass(frozen=True)
class LatAndLong:
    latitude: float
    longitude: float
    
    def __post_init__(self):
        """Validates the latitude and longitude."""
        if self.latitude is None or self.longitude is None:
            raise ValueError("Latitude or Longitude cannot be empty.")
        if not (-90 <= self.latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees.")
        if not (-180 <= self.longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180 degrees.")
        
    def values(self) -> list[float]:
        """Returns the latitude and longitude as a list."""
        return [self.latitude, self.longitude]