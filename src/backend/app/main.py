import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))


def main():
    from dependencies import get_store_service

    service = get_store_service()

    stores = service.get_all_stores()
    print(stores)


if __name__ == "__main__":
    main()
