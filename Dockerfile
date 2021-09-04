#syntax=docker/dockerfile:1
FROM python:3.10.0rc2

WORKDIR /app

RUN pip install poetry==1.2.0a2

COPY pyproject.toml .

RUN poetry install
