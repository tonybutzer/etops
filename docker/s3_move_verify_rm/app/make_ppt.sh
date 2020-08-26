#! /bin/bash


for i in {2006..2016} ; do  echo  python3 s3_move.py --src dev-et-data/in/north_america_data/precipitation/$i/ --dst dev-et-data/in/NorthAmerica/PPT/daily/$i/ \&; done
