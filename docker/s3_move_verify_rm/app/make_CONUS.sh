#! /bin/bash


for i in `cat jj`; do  echo  python3 s3_move.py --src dev-et-data/tiles/$i --dst dev-et-data/out/CONUS/Run_062720_tiles/$i \&; done
