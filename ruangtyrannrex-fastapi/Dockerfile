FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY ./app app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]