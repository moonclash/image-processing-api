import os
from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .services.file_io_service import FileIOService
from .services.helper_services import GoodMorningImage


app = FastAPI()

static_dir = os.path.dirname(__file__)
static_path = os.path.join(static_dir, "static/")
templates_path = os.path.join(static_dir, "templates/")

app.mount(os.path.join('/static'), StaticFiles(directory=static_path), name='static')
templates = Jinja2Templates(directory=templates_path)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'title': 'Good Morning'})


@app.post('/files')
async def upload_file(file: UploadFile):
    io_service = FileIOService()
    modified_image = GoodMorningImage.good_morningfy(file.file, file.filename)
    io_service.upload_file(modified_image, 'dobro-utro', modified_image)
    os.remove(modified_image)
    return {'url': f'https://dobro-utro.s3.eu-west-1.amazonaws.com/{modified_image}'}