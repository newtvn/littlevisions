FROM node:18-alpine

WORKDIR /app
COPY ./app/package*.json ./
RUN npm install
COPY ./app .


RUN npm run build
RUN npm install -g http-server

EXPOSE 8080
CMD [ "http-server", "dist" ]