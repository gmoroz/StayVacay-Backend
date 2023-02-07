alembic upgrade head
python loaddata.py
uvicorn app.main:app --host 0.0.0.0 --port $PORT --reload
