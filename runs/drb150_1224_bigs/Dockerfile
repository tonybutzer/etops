FROM tbutzer/et-base-python

ENV Test1=v1.0
ENV VERS=drb150_1224_bigs

RUN apt-get update && \
	apt-get install -y vim

ENV TONYVERS=6.9
RUN mkdir -p /home/veget \
	&& cd /home/veget\
	&& git clone http://github.com/skagone/cloud-veg-et \
	&& (cd /home/veget/cloud-veg-et/vegetLib; make build-root) \
	&& mkdir -p /home/veget/cloud-veg-et/api_veget/log

COPY running_config /home/veget/cloud-veg-et/api_veget/running_config

RUN apt-get install ca-certificates && mkdir -p /etc/pki/tls/certs && \
	cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt

WORKDIR /home/veget/cloud-veg-et/api_veget
