docker run -i -v `pwd`/AOI:/home/veget/cloud-veg-et/api_veget/AOI tbutzer/test_numeric_gridmeister_c python3 api_veget.py -c running_config -s ./AOI/run_test_numeric_gridmeister_c_chip42.78N-77.42E.shp  run_test_numeric_gridmeister_c_chip42.78N-77.42E  2>&1 | tee  ./log/run_test_numeric_gridmeister_c_chip42.78N-77.42E.log&
