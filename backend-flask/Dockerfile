FROM python:3.11.1-slim-buster


WORKDIR /backend

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root --only main

COPY . .

ENV PORT=8000
ENV FRONTEND_URL='*'
ENV BACKEND_URL='*'
EXPOSE $PORT
CMD uvicorn main:app --host=0.0.0.0 --port=$PORT --reload
