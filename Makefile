.PHONY: ruff fe

ruff:
	ruff check . --fix

fe:
	cd src/frontend/coding-test-fe && npm run dev
