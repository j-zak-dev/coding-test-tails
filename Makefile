.PHONY: ruff fe be

ruff:
	ruff check . --fix

fe:
	cd src/frontend/coding-test-fe && npm run dev

be:
	cd src/backend/entrypoints/api && fastapi dev
