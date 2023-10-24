# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
RUN mkdir /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH=/app/\
    PYTHONUNBUFFERED=1\
    POSTGRES_HOST_ADDRESS=supersonic-postgres\
    POSTGRES_DATABASE_NAME=social_db\
    POSTGRES_PASSWORD=123\
    POSTGRES_USERNAME=social_admin


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app/
