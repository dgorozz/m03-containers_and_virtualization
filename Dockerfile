FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN python -m pip install -r requirements.txt --no-cache-dir

COPY ./api ./api

CMD ["python", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
