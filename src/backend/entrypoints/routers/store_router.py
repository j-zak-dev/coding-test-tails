from typing import Annotated

from application.dtos.store_response_dto import EnrichedStoresByNamesRequestDTO
from application.services.store_service import StoreService
from dependencies import get_store_service
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


@router.get("/stores/enriched_search_by_name")
def get_enriched_stores_by_name_query(
    store_service: Annotated[StoreService, Depends(get_store_service)],
    name: str = "",
):
    normalized_name = name.strip()
    if not normalized_name:
        return store_service.get_all_stores()
    return store_service.get_enriched_stores(normalized_name)


@router.get("/stores/enriched_search_by_name/{name}")
def get_enriched_stores_by_name(
    name: str,
    store_service: Annotated[StoreService, Depends(get_store_service)],
):
    return store_service.get_enriched_stores(name)


@router.post("/stores/enriched_search_by_names")
def get_enriched_stores_by_names(
    payload: EnrichedStoresByNamesRequestDTO,
    store_service: Annotated[StoreService, Depends(get_store_service)],
):
    return store_service.get_enriched_stores_by_names(payload.storeNames)
