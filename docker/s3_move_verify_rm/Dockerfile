FROM python

ENV VERS=1.0

RUN apt-get update && \
        apt-get install -y vim

RUN \
        pip install --no-cache awscli && \
        pip install --no-cache s3fs && \
        pip install --no-cache boto3 

RUN mkdir -p /home

ENV TONYVERS=0.1

COPY app /home/app

WORKDIR /home/app


