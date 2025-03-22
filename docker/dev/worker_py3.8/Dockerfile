FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements/* /code/
RUN pip install -r dev.txt

RUN apt-get update && \
    apt-get --no-install-recommends install -q -y default-jre default-jdk \
    git cmake libeigen3-dev libboost-python-dev libopencv-dev python3-opencv \
    libgmp-dev libcgal-qt5-dev swig && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --only-binary=:all: PyYAML    
RUN pip install --upgrade pip setuptools==65.5.0 wheel && pip install --upgrade cython && pip install -U cffi service_identity numpy>=1.18
RUN pip install -r worker.txt

ADD . /code

CMD ["./docker/wait-for-it.sh", "django:8000", "--", "python", "-m", "scripts.workers.submission_worker"]

# Use the latest stable Python version
# FROM python:3.12-slim

# ENV PYTHONUNBUFFERED=1

# # Set work directory
# WORKDIR /code

# # Copy dependencies first for better caching
# ADD requirements/* /code/

# # Upgrade pip and install dependencies
# RUN pip install --upgrade pip && pip install -r dev.txt

# # Install required system packages
# RUN apt-get update && \
#     apt-get install --no-install-recommends -y \
#     default-jre default-jdk git cmake libeigen3-dev \
#     libboost-python-dev libopencv-dev python3-opencv \
#     libgmp-dev libcgal-qt5-dev swig && \
#     rm -rf /var/lib/apt/lists/*

# # Install additional Python dependencies
# RUN pip install -U cffi service_identity cython==0.29 numpy==1.14.5
# RUN pip install -r worker.txt

# # Copy the rest of the application code
# ADD . /code

# # Ensure the script is executable
# RUN chmod +x ./docker/wait-for-it.sh

# # Define entrypoint command
# CMD ["./docker/wait-for-it.sh", "django:8000", "--", "python", "-m", "scripts.workers.submission_worker"]
