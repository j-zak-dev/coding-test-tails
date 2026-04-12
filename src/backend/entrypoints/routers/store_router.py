from typing import Annotated

from application.services.store_service import StoreService
from backend.dependencies import get_store_service
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/stores")
def get_all_stores(
    store_service: Annotated[StoreService, Depends(get_store_service)],
):
    return store_service.get_all_stores()


@router.get("/stores/search_by_name/{name}")
def search_stores_by_name(
    name: str,
    store_service: Annotated[StoreService, Depends(get_store_service)],
):
    return store_service.search_stores_by_name(name)


@router.get("/stores/search_by_postcode/{postcode}")
def search_store_by_postcode(
    postcode: str,
    store_service: Annotated[StoreService, Depends(get_store_service)],
):
    return store_service.search_store_by_postcode(postcode)
