from domain.aggregates.store import RichStore, Store
from domain.valueObjects.latAndLong import LatAndLong


def map_store_to_domain_store(store_data) -> Store:
    id = store_data.get("id")  ## TO DO: This should be generated in the repository, not the mapper.
    name = store_data.get("name")
    postcode = store_data.get("postcode")

    return Store(id=id, name=name, postcode=postcode)


def map_store_to_domain_rich_store(store_data) -> Store:
    id = store_data.get("id")  ## TO DO: This should be generated in the repository, not the mapper.
    name = store_data.get("name")
    postcode = store_data.get("postcode")

    ## Constructor could be more defensive however we always have lat and long based on how the get function works.
    latAndLong = LatAndLong(
        latitude=store_data.get("latAndLong")[0], longitude=store_data.get("latAndLong")[1]
    )

    return RichStore(id=id, name=name, postcode=postcode, latAndLong=latAndLong)
