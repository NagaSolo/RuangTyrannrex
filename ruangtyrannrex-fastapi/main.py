from typing import Optional

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory='./modules/static'), name='style.css')
templates = Jinja2Templates(directory='./modules/templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request' : request})

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}