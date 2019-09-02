FROM continuumio/miniconda3

EXPOSE 8000

# Install apache2 web server and apache2-dev module
# Then totally clean up apt-get remainings
RUN apt-get update && apt-get install -y apache2 \
    apache2-dev \
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

# For apache to work, the app and related files must be in /var/www
WORKDIR /var/www/text_cluster_api/
COPY ./text_cluster_api.wsgi /var/www/text_cluster_api/text_cluster_api.wsgi
COPY ./flask_api /var/www/text_cluster_api/

RUN pip install -r requirements.txt

# Install/enable mod_wsgi module (installed via pip just above) on the apache end
RUN /opt/conda/bin/mod_wsgi-express install-module

# Set up apache server by invoking our .wsgi file
RUN mod_wsgi-express setup-server text_cluster_api.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80

# Start apache web server in the foreground
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND