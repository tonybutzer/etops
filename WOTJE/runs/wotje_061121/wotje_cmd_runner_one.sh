docker run -i -v `pwd`/AOI:/home/veget/cloud-veg-et-basin/api_veget/AOI tbutzer/wotje_061121 python3 api_veget.py -c running_config -s ./AOI/extent.shp  run_wotje_06142021  2>&1 | tee  ./log/run_wotje_061421.log&
