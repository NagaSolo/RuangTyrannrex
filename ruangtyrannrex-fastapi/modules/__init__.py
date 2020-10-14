from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# app.mount('/static', StaticFiles(directory='./modules/static', name='static'))
templates = Jinja2Templates(directory='/modules/templates')

from modules.views import main