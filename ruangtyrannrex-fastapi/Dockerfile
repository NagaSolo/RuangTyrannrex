FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY app .

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5002

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]
