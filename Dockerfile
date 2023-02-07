FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /code

COPY ./app /code/
COPY ./allembic /code/
COPY entrypoint.sh .

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
