from typing import Optional

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='./templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request' : request})

@app.get('/fortytwo', response_class=HTMLResponse)
async def fortytwo_route(request: Request):
    return templates.TemplateResponse('fortytwo.html', {'request' : request})

@app.get('/flow007', response_class=HTMLResponse)
async def flow_007(request: Request):
    return templates.TemplateResponse('flow007.html', {'request' : request})

@app.get('/lapindromes', response_class=HTMLResponse)
async def lapindromes(request: Request):
    return templates.TemplateResponse('lapindromes.html', {'request' : request})

@app.get('/zco14003', response_class=HTMLResponse)
async def opt_prices(request: Request):
    return templates.TemplateResponse('zco14003.html', {'request' : request})

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}