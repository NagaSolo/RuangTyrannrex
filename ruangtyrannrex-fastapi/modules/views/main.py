from modules import app, templates

from typing import Optional
from fastapi import Request

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html')

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}