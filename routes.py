from fastapi import APIRouter
from model import Quote

quotes_router = APIRouter()

quote_list = []

@quotes_router.post("/quotes")
async def add_quote(quote: Quote) -> dict:
    quote_list.append(quote)
    return {"message": "Quote added correctly"}
