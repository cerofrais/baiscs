import torch
from app.config import MODEL_PATH

from torchvision.models import resnet50, ResNet50_Weights
import os

# model = resnet50(weights=ResNet50_Weights.DEFAULT)

# torch.save(model, "classifier.pth")
model = torch.load(MODEL_PATH, weights_only=False)




def predict_image(image_tensor):
    with torch.no_grad():
        output = model(image_tensor)
        _, predicted = torch.max(output, 1)
    return predicted.item()
