from fastapi import APIRouter

# Create a router for Welcome
solana_router = APIRouter(prefix="/solana", tags=["Solana"])


@solana_router.get("/items/{item_id}")
def read_solana_item(item_id: int, q: str = None):
    return {"blockchain": "Solana", "item_id": item_id, "q": q}
