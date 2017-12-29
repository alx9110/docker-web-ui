FROM ubuntu:trusty
ENV DEBIAN_FRONTEND noninteractive
EXPOSE 80
RUN locale-gen ru_RU.UTF-8 && dpkg-reconfigure locales; \
echo 'Europe/Moscow' > /etc/timezone && dpkg-reconfigure tzdata
RUN apt-get update -qq; \
    apt-get -y --force-yes install software-properties-common; \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7FCD11186050CD1A ; \
    apt-get update -qq
RUN apt-get install -y supervisor nginx && \
    echo "daemon off;" >> /etc/nginx/nginx-default.conf
RUN apt-get -y --force-yes install python-virtualenv uwsgi uwsgi-plugin-python
COPY uwsgi/uwsgi.ini /srv/uwsgi.ini
COPY nginx/nginx.conf /etc/nginx/sites-enabled/nginx.conf
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/lib/nginx
RUN mkdir -p /var/lib/nginx/body
RUN mkdir -p /var/lib/nginx/fastcgi
CMD ["/usr/bin/supervisord"]