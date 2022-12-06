from fastapi import FastAPI, UploadFile
from services.image_processing_service import ImageProcessingService
from services.file_io_service import FileIOService
from services.helper_services import GoodMorningImage
import uuid

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/files/')
async def upload_file(upload_file: UploadFile):
    io_service = FileIOService()
    GoodMorningImage.good_morningfy(upload_file.file)
    name = str(uuid.uuid4())
    io_service.upload_file('new.jpeg', 'dobro-utro', f'{name}.jpeg')
    return {'filename': f'https://dobro-utro.s3.eu-west-1.amazonaws.com/{name}.jpeg'}