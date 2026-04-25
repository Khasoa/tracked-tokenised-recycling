from fastapi import FastAPI

app = FastAPI(
    title="Tracked Recycling API"
)


@app.get("/")
def root():
    return {"message": "API running"}