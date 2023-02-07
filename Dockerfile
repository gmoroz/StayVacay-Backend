FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /code/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]
