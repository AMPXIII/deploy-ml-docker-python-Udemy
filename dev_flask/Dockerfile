FROM continuumio/miniconda3

COPY flask_demo /usr/local/python/

EXPOSE 5000

WORKDIR /usr/local/python/
RUN pip install -r requirements.txt


CMD python flask_RF.py