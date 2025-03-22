# FROM python:3.10

# ENV PYTHONUNBUFFERED 1

# RUN mkdir /code
# WORKDIR /code
# ADD requirements/* /code/
# RUN pip install -r prod.txt

# ADD . /code

# CMD ["sh", "/code/docker/prod/django/container-start.sh"]

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Copy only requirements first for caching dependencies
ADD requirements/* /code/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r prod.txt

# Copy the rest of the application code
ADD . /code

# Set entrypoint
CMD ["sh", "/code/docker/prod/django/container-start.sh"]
