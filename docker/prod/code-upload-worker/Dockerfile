# FROM python:3.10

# ENV PYTHONUNBUFFERED 1

# RUN mkdir /code
# WORKDIR /code

# RUN apt-get update && \
#   apt-get install --no-install-recommends -y unzip && \
#   rm -rf /var/lib/apt/lists/*

# ADD requirements/* /code/

# RUN pip install -r code_upload_worker.txt

# ADD . /code

# RUN chmod +x scripts/workers/code_upload_worker_utils/install_dependencies.sh

# CMD ["scripts/workers/code_upload_worker_utils/install_dependencies.sh"]

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install required system dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y unzip && \
    rm -rf /var/lib/apt/lists/*

# Copy dependencies first for better caching
ADD requirements/* /code/

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r code_upload_worker.txt

# Copy the rest of the application code
ADD . /code

# Ensure script has execution permissions
RUN chmod +x scripts/workers/code_upload_worker_utils/install_dependencies.sh

# Set entrypoint
CMD ["sh", "scripts/workers/code_upload_worker_utils/install_dependencies.sh"]
