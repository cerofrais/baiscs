from fastapi import FastAPI
from app.routers import predict


app = FastAPI()

app.include_router(predict.router)

@app.get("/health")
def read_root():
    return {"message": "Image Classifier API is up and running"}
