FROM node:14.20.0

# install chrome for protractor tests
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update && apt-get install -yq google-chrome-stable

WORKDIR /code

# Add dependencies
ADD ./package.json /code
ADD ./bower.json /code
ADD ./gulpfile.js /code
ADD ./.eslintrc /code
ADD ./karma.conf.js /code

# Install Prerequisites
RUN npm install -g bower gulp gulp-cli

RUN npm link gulp

RUN npm cache clean -f
RUN npm install
RUN npm install -g karma-cli
RUN npm install -g qs
RUN bower install --allow-root
RUN apt-get install -y libxss1

CMD ["gulp", "dev:runserver"]

EXPOSE 8888

# Use the latest stable Node.js version
# FROM node:20-slim

# # Install Chrome for Protractor tests
# RUN apt-get update && \
#     apt-get install -y wget gnupg libxss1 && \
#     wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#     sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list' && \
#     apt-get update && \
#     apt-get install -y google-chrome-stable && \
#     rm -rf /var/lib/apt/lists/*

# # Set working directory
# WORKDIR /code

# # Copy dependencies first to leverage caching
# COPY package.json bower.json gulpfile.js .eslintrc karma.conf.js /code/

# # Install global dependencies
# RUN npm install -g bower gulp gulp-cli karma-cli qs

# # Install project dependencies
# RUN npm install && \
#     bower install --allow-root && \

#     npm cache clean --force

# # Expose application port
# EXPOSE 8888

# # Default command
# CMD ["gulp", "dev:runserver"]
