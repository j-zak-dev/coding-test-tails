import json
import os
from pathlib import Path

from application.services.store_service import StoreService
from domain.interfaces.storeInterface import StoreInterface
from infrastructure.repositories.stores_repo import StoresRepo
from infrastructure.services.clients.mocky_postcode_io_client import get_mocky_postcode_io_response
from infrastructure.services.clients.postcodes_io_client import get_lat_and_long_from_postcode

BACKEND_ROOT = Path(__file__).resolve().parent


def _load_env_file() -> None:
    env_path = BACKEND_ROOT / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue

        key, value = stripped.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ.setdefault(key, value)


_load_env_file()


def get_store_repository() -> StoreInterface:
    data_path = BACKEND_ROOT / "infrastructure" / "data" / "stores.json"
    with data_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    use_mocky_postcodes = os.getenv("MOCKY_POSTCODES", "").strip().lower() == "true"

    if use_mocky_postcodes:
        print("Using mocky_postcode_io_client for coordinates")
        coords_fn = get_mocky_postcode_io_response
    else:
        print("Using postcodes_io_client for coordinates")
        coords_fn = get_lat_and_long_from_postcode

    return StoresRepo(get_coords_fn=coords_fn, data=data)


def get_store_service() -> StoreService:
    store_repository = get_store_repository()
    return StoreService(store_repository=store_repository)
