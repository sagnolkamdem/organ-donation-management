from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Organ Donation Management API")

#les routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Organ Donation Management API"}

