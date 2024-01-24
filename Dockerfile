# pull official base image
FROM python:3.10.4-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN set -xe \
    && apt update \
    && apt install -y --no-install-recommends build-essential \
    && pip install virtualenvwrapper poetry==1.4.2 \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY ./pyproject.toml .

RUN poetry install 

# Copy project files
COPY . .

# Collect static files
RUN pwd
RUN ls -la
RUN cd ***_backend
RUN pwd

# RUN poetry run python -m ***_backend.manage collectstatic --noinput


