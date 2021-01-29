#! /bin/bash

sudo mkdir -p /mnt/dev-et-data
sudo chown ubuntu:ubuntu /mnt/dev-et-data
REGION=us-west-2

sudo s3fs -o allow_other -o iam_role="lsds-developer-ec2" \
-o use_cache=/tmp \
-o url="https://s3-$REGION.amazonaws.com" \
-o umask=0227,uid=1000 \
-o nonempty     \
        dev-et-data /mnt/dev-et-data
