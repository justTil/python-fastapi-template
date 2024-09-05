from fastapi import APIRouter

# Create a router for Bitcoin
bitcoin_router = APIRouter(prefix="/bitcoin", tags=["Bitcoin"])


@bitcoin_router.get("/items/{item_id}")
def read_bitcoin_item(item_id: int, q: str = None):
    return {"blockchain": "Bitcoin", "item_id": item_id, "q": q}
