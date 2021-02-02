FROM python

ENV VERS=RUNN

RUN apt-get update && \
        apt-get install -y vim && \
        apt-get install -y libgdal-dev

RUN \
        pip install --no-cache matplotlib && \
        pip install --no-cache matplotlib_venn && \
        pip install --no-cache pandas && \
        pip install --no-cache geopandas && \
        pip install --no-cache seaborn && \
        pip install --no-cache plotly && \
        pip install --no-cache plotly.express && \
        pip install "rasterio<1.2.0" && \
        pip install --no-cache awscli && \
        pip install --no-cache s3fs && \
        pip install --no-cache ffmpeg && \
        pip install --no-cache pika && \
        pip install --no-cache dash && \
        pip install --no-cache boto3 && \
        pip install --no-cache fiona



