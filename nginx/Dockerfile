FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
WORKDIR /var/www/
RUN mkdir .well-known
COPY /.well-known /var/www/.well-known/