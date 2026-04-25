from fastapi import FastAPI

app = FastAPI(title="Tracked Tokenised Recycling API")

@app.get("/")
def root():
    return {"message": "API running"}