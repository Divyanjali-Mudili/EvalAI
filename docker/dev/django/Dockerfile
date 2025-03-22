# FROM python:3.10 

# ENV PYTHONUNBUFFERED 1
# WORKDIR /code

# # Copy requirements first (for efficient Docker layer caching)
# ADD requirements/* /code/


# # Upgrade pip, setuptools, and wheel to avoid installation issues
# RUN pip install --upgrade pip setuptools wheel && pip install cython && apt-get update && apt-get install -y build-essential python3-dev
# RUN pip install --no-cache-dir --only-binary=:all: PyYAML

# # Install remaining dependencies
# RUN pip install -r dev.txt

# # Start the application with dependency checks
# CMD ["./docker/wait-for-it.sh", "db:5432", "--", "sh", "/code/docker/dev/django/container-start.sh"]



FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements/* /code/
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpcre3 \
    libpcre3-dev \
    libssl-dev \
    zlib1g-dev \
    libffi-dev \
    gcc

RUN pip install --upgrade setuptools>=65.5.0 pip wheel==0.40.0 && apt-get update && apt-get install -y uwsgi uwsgi-plugin-python3
RUN pip install --no-cache-dir --no-binary uwsgi uwsgi

RUN apt-get update && \
    apt-get --no-install-recommends install -q -y default-jre default-jdk \
    git cmake libeigen3-dev libboost-python-dev libopencv-dev python3-opencv \
    libgmp-dev libcgal-qt5-dev swig && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    python3-dev gcc build-essential libssl-dev libpcre3-dev libsystemd-dev libffi-dev && apt-get update && apt-get install -y build-essential python3-dev libpcre3 libpcre3-dev
RUN pip install -r dev.txt
CMD ["./docker/wait-for-it.sh", "db:5432", "--", "sh", "/code/docker/dev/django/container-start.sh"]

# pip install --no-cache-dir "uwsgi<2.0.21" || echo "uWSGI install failed, skipping" && 
# FROM python:3.12-slim

# ENV PYTHONUNBUFFERED 1

# RUN mkdir /code
# WORKDIR /code

# ADD requirements/* /code/
# RUN pip install --upgrade pip setuptools wheel --timeout=100 && apt-get update && apt-get install -y libcurl4-openssl-dev
# RUN pip install cython && pip install PyYAML==5.4.1
# RUN pip install --upgrade djangorestframework-expiring-authtoken && pip install -r dev.txt

# CMD ["./docker/wait-for-it.sh", "db:5432", "--", "sh", "/code/docker/dev/django/container-start.sh"]

# RUN pip install --upgrade pip setuptools wheel
# FROM python:3.10

# ENV PYTHONUNBUFFERED 1

# WORKDIR /code

# COPY requirements/ /code/
# RUN pip install --upgrade pip setuptools==65.5.0 wheel && pip install -r dev.txt

# COPY . /code/

# CMD exec ./docker/wait-for-it.sh db:5432 -- sh /code/docker/dev/django/container-start.sh

# Use the latest stable Python version
# FROM python:3.12-slim

# ENV PYTHONUNBUFFERED=1

# # Set work directory
# WORKDIR /code

# # Copy and install dependencies first for better caching
# COPY requirements/ /code/
# RUN pip install --upgrade pip setuptools==65.5.0 wheel && pip install -r dev.txt

# # Copy the rest of the application code
# COPY . /code/

# # Ensure the script is executable
# RUN chmod +x ./docker/wait-for-it.sh
# RUN chmod +x /code/docker/dev/django/container-start.sh

# # Define entrypoint command
# CMD exec ./docker/wait-for-it.sh db:5432 -- sh /code/docker/dev/django/container-start.sh

# Use the latest stable Python 3.12-slim image
# FROM python:3.12-slim

# # Set environment variables
# ENV PYTHONUNBUFFERED=1 \
#     PIP_NO_CACHE_DIR=1 \
#     DEBIAN_FRONTEND=noninteractive

# # Set the working directory
# WORKDIR /code

# # Install required system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc libpq-dev build-essential curl && \
#     rm -rf /var/lib/apt/lists/*

# # Upgrade pip and install dependencies in a virtual environment
# COPY requirements/ /code/
# RUN pip install --upgrade pip setuptools wheel && pip install -r dev.txt

# # Copy the rest of the application code
# COPY . /code/

# # Ensure the startup script is executable
# RUN chmod +x ./docker/wait-for-it.sh
# RUN chmod +x /code/docker/dev/django/container-start.sh

# # Expose Django’s default port
# EXPOSE 8000

# # Start Django application
# CMD ["./docker/wait-for-it.sh", "db:5432", "--", "sh", "/code/docker/dev/django/container-start.sh"]
