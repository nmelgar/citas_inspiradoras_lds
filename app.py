from fastapi import FastAPI
from routes import quotes_router

app = FastAPI()

app.include_router(quotes_router)

