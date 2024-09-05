from fastapi import APIRouter

# Create a router for Ethereum
ethereum_router = APIRouter(prefix="/ethereum", tags=["Ethereum"])


@ethereum_router.get("/items/{item_id}")
def read_ethereum_item(item_id: int, q: str = None):
    return {"blockchain": "Ethereum", "item_id": item_id, "q": q}
