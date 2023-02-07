FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

ENV PYTHONPATH "${PYTHONPATH}:/"

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app/

ENTRYPOINT ["sh", "entrypoint.sh"]
