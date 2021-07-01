FROM tbutzer/et-base-python

ENV VERS=wotje061021_2

ENV TONYVERS=6.9
RUN mkdir -p /home/veget \
	&& cd /home/veget\
	&& git clone https://github.com/skagone/cloud-veg-et-basin.git \
	&& (cd /home/veget/cloud-veg-et-basin/vegetLib; make build-root) \
	&& mkdir -p /home/veget/cloud-veg-et-basin/api_veget/log

COPY running_config /home/veget/cloud-veg-et-basin/api_veget/running_config

RUN apt-get install ca-certificates && mkdir -p /etc/pki/tls/certs && \
	cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt

WORKDIR /home/veget/cloud-veg-et-basin/api_veget


