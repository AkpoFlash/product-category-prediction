import model
from fastapi import BackgroundTasks, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/download-image-set")
async def download_image_set(background_tasks: BackgroundTasks):
    background_tasks.add_task(model.download_image_set)
    return {"message": "Downloading of image set are sending in the background"}


@app.post("/export-model")
async def export_model(background_tasks: BackgroundTasks):
    background_tasks.add_task(model.export_model)
    return {"message": "Model exporting are sending in the background"}
