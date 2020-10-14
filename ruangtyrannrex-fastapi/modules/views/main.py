from modules import app, templates

from typing import Optional

from fastapi.requests import Request

from fastapi.responses import HTMLResponse

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request' : request})

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}