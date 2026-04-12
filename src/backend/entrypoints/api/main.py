from fastapi import FastAPI

from entrypoints.routers import store_router

app = FastAPI()

app.include_router(store_router.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
