import base64
import io
import model
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastai.vision.core import PILImage

class ClissifyImagePostBodyData(BaseModel):
    image: Union[str, None] = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/classify-image")
async def classify_image(item: ClissifyImagePostBodyData):
    img_file = io.BytesIO(base64.b64decode(item.image))
    return {"message": model.classify_image(PILImage.create(img_file))}
