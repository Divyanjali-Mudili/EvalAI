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

FROM python:3.9

ENV PYTHONUNBUFFERED=1

# Create and set working directory
RUN mkdir /code
WORKDIR /code

# Install unzip and clean up apt cache to reduce image size
RUN apt-get update && \
    apt-get install --no-install-recommends -y unzip && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements/code_upload_worker.txt /code/

RUN pip install --no-cache-dir -r /code/code_upload_worker.txt

# Copy the rest of the application code
COPY . /code

# Set script executable permissions
RUN chmod +x /code/scripts/workers/code_upload_worker_utils/install_dependencies.sh

# Use ENTRYPOINT to ensure the shell script is always executed
ENTRYPOINT ["/code/scripts/workers/code_upload_worker_utils/install_dependencies.sh"]

# If you want the container to run indefinitely or a process, 
# you can add a default command, such as:
# CMD ["tail", "-f", "/dev/null"]  # Optional if you want the container to stay alive for debugging.
