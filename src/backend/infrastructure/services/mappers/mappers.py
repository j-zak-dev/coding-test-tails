import uuid

from domain.aggregates.store import Store
from domain.valueObjects.latAndLong import LatAndLong


def map_store_to_domain(store_data) -> Store:
    name = store_data.get("name")
    postcode = store_data.get("postcode")

    ## Constructor could be more defensive however we always have lat and long based on how the get function works.
    latAndLong = LatAndLong(
        latitude=store_data.get("latAndLong")[0], longitude=store_data.get("latAndLong")[1]
    )

    return Store(id=uuid.uuid4(), name=name, postcode=postcode, latAndLong=latAndLong)
