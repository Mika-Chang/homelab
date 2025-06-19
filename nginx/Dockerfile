FROM nginx:1.27.5-alpine
COPY ./mySite /var/www/mySite
COPY ./conf/portfolio-mikacc.xyz.conf /etc/nginx/conf.d/mikacc.xyz.conf
RUN apk update && apk upgrade && apk add curl
RUN rm /etc/nginx/conf.d/default.conf
