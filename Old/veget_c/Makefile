Image=tbutzer/veget_c

build:
	docker build -t ${Image} .

run:
	docker run -it ${Image} bash

exec:
	docker exec -it ${Image} bash

git:
	(cd /opt/etops ; make)


dela_logs:
	docker run -i ${Image} python3 api_veget.py -c delaware_config -s DRB.shp lilDRB_temp
