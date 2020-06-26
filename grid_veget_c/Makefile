Image=tbutzer/drb_veget_c

build:
	docker build -t ${Image} .

run:
	docker run -it ${Image} bash

exec:
	docker exec -it ${Image} bash

git:
	(cd /opt/etops ; make)


dela_logs:
	docker run -i ${Image} python3 api_veget.py -c running_config -s AOI/d40N-78E.shp tile40N-80E_chip40N-78E

