FROM python

RUN \
	pip install --no-cache matplotlib && \
	pip install --no-cache matplotlib_venn && \
	pip install --no-cache pandas && \
	pip install --no-cache seaborn && \
	pip install --no-cache plotly && \
	pip install --no-cache plotly.express && \
	pip install --no-cache rasterio && \
	pip install --no-cache awscli && \
	pip install --no-cache s3fs && \
	pip install --no-cache ffmpeg && \
	pip install --no-cache pika && \
	pip install --no-cache dash && \
	pip install --no-cache boto3


RUN mkdir -p /home/veget && cd /home/veget && git clone http://github.com/skagone/cloud-veg-et 
