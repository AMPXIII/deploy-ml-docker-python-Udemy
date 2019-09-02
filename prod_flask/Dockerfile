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
WORKDIR /var/www/flask_RF/
COPY ./flask_RF.wsgi /var/www/flask_RF/flask_RF.wsgi
COPY ./flask_demo /var/www/flask_RF/

RUN pip install -r requirements.txt

# Install/enable mod_wsgi module (installed via pip just above) on the apache end
RUN /opt/conda/bin/mod_wsgi-express install-module

# Set up apache server by invoking our .wsgi file
# The port flag overrides whatever port we specified inside the flask python script
# Good security practive: Impose user and user group so that the apache server does not use root
# We specify the server root folder so that logs and application level files are safely kept
# in a folder of our choice (if not, they go to tmp, and might get accidentally deleted)
RUN mod_wsgi-express setup-server flask_RF.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80

# Start apache web server in the foreground
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND