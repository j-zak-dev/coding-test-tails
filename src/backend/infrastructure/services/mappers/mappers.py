import uuid

from domain.aggregates.store import Store
from infrastructure.services.clients.postcodes_io_client import get_lat_and_long_from_postcode


def map_store_to_domain(store_data) -> Store:
    name = store_data.get("name")
    postcode = store_data.get("postcode")
    latAndLong = get_lat_and_long_from_postcode(store_data.get("postcode"))

    return Store(id=uuid.uuid4(), name=name, postcode=postcode, latAndLong=latAndLong)
