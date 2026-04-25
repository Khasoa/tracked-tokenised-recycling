from fastapi import FastAPI
from app.controllers.auth_controller import router as auth_router

app = FastAPI(title="Tracked Recycling API")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "API running"}