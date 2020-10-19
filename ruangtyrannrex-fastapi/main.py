from typing import Optional

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse

from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from modules.fortytwo import fortytwo
from modules.flow007 import reversal
from modules.lapindromes import palindrome
# from modules.zco14003 import zco14003

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='./templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request' : request})

@app.get('/fortytwo', response_class=HTMLResponse)
async def fortytwo_route(request: Request):
    return templates.TemplateResponse('fortytwo.html', {'request' : request})

@app.post('/fortytwo', response_class=HTMLResponse)
async def fortytwo_post(request: Request, the_answer: int = Form(...)):
    answer = fortytwo(the_answer)
    return templates.TemplateResponse('fortytwo.html', context={'request' : request, 'answer' : answer})

@app.get('/flow007', response_class=HTMLResponse)
async def flow_007(request: Request):
    return templates.TemplateResponse('flow007.html', {'request' : request})

@app.get('/lapindromes', response_class=HTMLResponse)
async def lapindrome(request: Request):
    return templates.TemplateResponse('lapindromes.html', {'request' : request})

@app.get('/zco14003', response_class=HTMLResponse)
async def opt_prices(request: Request):
    return templates.TemplateResponse('zco14003.html', {'request' : request})

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}