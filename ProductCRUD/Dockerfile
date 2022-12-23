FROM python:3.10-slim-bullseye

WORKDIR /usr/src/productCRUD

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir staticfiles

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/productCRUD/entrypoint.sh
RUN chmod +x /usr/src/productCRUD/entrypoint.sh

COPY . .