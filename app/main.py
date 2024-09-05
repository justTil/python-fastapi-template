from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes_solana import solana_router
from app.api.routes_ethereum import ethereum_router
from app.api.routes_bitcoin import bitcoin_router

app = FastAPI(
    title="FastAPI with Swagger UI Template",
    description="FastAPI template.",
    summary="This template is provided by Alator Genesis for the FastAPI framework with Swagger UI.",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Alator Genesis",
        "url": "https://alatorgenesis.com/",
        "email": "contact@alatorgenesis.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/fastapi/fastapi/blob/master/LICENSE",
    },
)

# Redirect from the root URL to the /docs page


@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")


# Include the Bitcoin router
app.include_router(bitcoin_router)

# Include the Ethereum router
app.include_router(ethereum_router)

# Include the Solana router
app.include_router(solana_router)
