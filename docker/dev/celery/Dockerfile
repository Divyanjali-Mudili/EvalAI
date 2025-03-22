# FROM python:3.11

# ENV PYTHONUNBUFFERED 1

# RUN apt-get update
# RUN mkdir /code
# WORKDIR /code

# ADD requirements/* /code/

# RUN pip install -r dev.txt

# CMD ["./docker/wait-for-it.sh", "django:8000", "--", "sh", "/code/docker/dev/celery/container-start.sh"]

FROM python:3.9

ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code

# Install system dependencies and clean up apt cache to reduce image size
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    # Add any system dependencies you need here (e.g., curl, netcat, etc.)
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements/* /code/

RUN pip install --no-cache-dir -r /code/dev.txt

# Copy the rest of the application code
COPY . /code

# Ensure wait-for-it.sh script has executable permissions
RUN chmod +x /code/docker/wait-for-it.sh

# Use the entrypoint for the container startup logic
CMD ["./docker/wait-for-it.sh", "django:8000", "--", "sh", "/code/docker/dev/celery/container-start.sh"]
