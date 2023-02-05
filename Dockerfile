FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

ENV PYTHONPATH "${PYTHONPATH}:/"

COPY ./app /app
COPY entrypoint.sh .

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
