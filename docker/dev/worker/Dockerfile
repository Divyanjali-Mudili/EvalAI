# FROM python:3.10

# ENV PYTHONUNBUFFERED 1

# RUN apt-get update && \
#     apt-get install -q -y default-jre default-jdk && \
#     rm -rf /var/lib/apt/lists/*

# RUN mkdir /code
# WORKDIR /code

# ADD requirements/* /code/

# RUN apt-get update && apt-get install -y libyaml-dev && apt-get update && apt-get install -y \
# build-essential \
# python3-dev \
# libffi-dev \
# libssl-dev \
# zlib1g-dev


# RUN apt-get update && apt-get install -y \
#     python3-dev gcc build-essential libssl-dev libpcre3-dev libsystemd-dev libffi-dev

# # Upgrade pip, setuptools, and wheel to avoid installation issues
# RUN pip install --upgrade pip setuptools>=65.5.0 wheel && pip install cython && pip install -U cffi service_identity numpy>=1.18

# # RUN pip install --no-cache-dir --no-binary PyYAML PyYAML
# RUN apt-get update && apt-get install -y uwsgi uwsgi-plugin-python3 
# # Install uWSGI separately to debug potential failures
# RUN pip install --no-cache-dir "uWSGI==2.0.20" || echo "uWSGI install failed, skipping"

# RUN pip install -r dev.txt
# RUN pip install -r worker.txt

# ADD . /code

# CMD ["./docker/wait-for-it.sh", "django:8000", "--", "python", "-m", "scripts.workers.submission_worker"]


# RUN pip install --no-cache-dir --only-binary=:all: PyYAML
# RUN pip install --no-cache-dir PyYAMl

# RUN apt-get update && \
#     apt-get --no-install-recommends install -q -y default-jre default-jdk \
#     git cmake libeigen3-dev libboost-python-dev libopencv-dev python3-opencv \
#     libgmp-dev libcgal-qt5-dev swig && \
#     rm -rf /var/lib/apt/lists/*

# RUN apt-get update && apt-get install -y python3-dev gcc libffi-dev libyaml-dev

# RUN pip install --upgrade pip setuptools==65.5.0 wheel && pip install --upgrade cython && pip install -U cffi service_identity numpy>=1.18
# RUN pip install --no-cache-dir --only-binary=:all: PyYAML
# RUN apt-get update && apt-get install -y uwsgi uwsgi-plugin-python3
# # Install uWSGI separately to debug potential failures
# RUN pip install --no-cache-dir "uWSGI==2.0.20" || echo "uWSGI install failed, skipping"


# Use the latest stable Python version
FROM python:3.9

ENV PYTHONUNBUFFERED=1

# Install system dependencies (default-jre, default-jdk)
RUN apt-get update && \
    apt-get install --no-install-recommends -y default-jre default-jdk && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /code

# Copy dependency files first to leverage Docker layer caching
ADD requirements/* /code/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -U cffi service_identity cython==0.29.21 numpy==1.21.6
RUN pip install -r dev.txt
RUN pip install -r worker.txt

# Copy the rest of the application code
ADD . /code

# Ensure the script is executable
RUN chmod +x ./docker/wait-for-it.sh

# Define entrypoint command
CMD ["./docker/wait-for-it.sh", "django:8000", "--", "python", "-m", "scripts.workers.submission_worker"]
