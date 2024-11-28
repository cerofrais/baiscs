from fastapi import APIRouter, File, UploadFile
from app.utils.inference import predict_image
from app.utils.preprocessing import preprocess_image

router = APIRouter()
import requests

# URL for ImageNet class index file
url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"

# Download and load class labels
imagenet_classes = requests.get(url).json()


@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = preprocess_image(await file.read())
    prediction_idx = predict_image(image)
    predicted_class = imagenet_classes[prediction_idx]
    return {"prediction": predicted_class }
