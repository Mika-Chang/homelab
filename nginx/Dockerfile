FROM nginx:1.27.5-alpine
COPY ./mySite /var/www/mySite
COPY ./mikacc.xyz.conf /etc/nginx/conf.d
RUN rm /etc/nginx/conf.d/default.conf
