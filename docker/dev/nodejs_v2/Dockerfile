# FROM node:20-slim

# RUN npm install -g @angular/cli@7.3.9
# WORKDIR /code

# ADD frontend_v2/package.json frontend_v2/yarn.lock /code/
# RUN yarn install
# ENV PATH="/code/node_modules/.bin:$PATH" 

# CMD ["yarn","start", "--verbose", "--host", "0.0.0.0"]


# Upgrade to the latest LTS version of Node.js
FROM node:14.20.0

# Install Angular CLI globally
RUN npm install -g @angular/cli@7.3.9

# Set work directory
WORKDIR /code

# Copy only dependency files first for better caching
COPY frontend_v2/package.json frontend_v2/yarn.lock /code/

# Install dependencies
RUN yarn install --frozen-lockfile

# Set PATH for globally installed packages
ENV PATH="/code/node_modules/.bin:$PATH"

# Expose development server port
EXPOSE 8888

# Default command to start the app
CMD ["yarn", "start", "--verbose", "--host", "0.0.0.0"]
