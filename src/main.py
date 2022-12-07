import os
from fastapi import FastAPI, UploadFile
from services.file_io_service import FileIOService
from services.helper_services import GoodMorningImage

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/files/')
async def upload_file(upload_file: UploadFile):
    io_service = FileIOService()
    modified_image = GoodMorningImage.good_morningfy(upload_file.file, upload_file.filename)
    io_service.upload_file(modified_image, 'dobro-utro', modified_image)
    os.remove(modified_image)
    return {'url': f'https://dobro-utro.s3.eu-west-1.amazonaws.com/{modified_image}'}