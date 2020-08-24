Image=tbutzer/veget_fork

build:
	docker build -t ${Image} .

run:
	docker run -it ${Image} bash

exec:
	docker exec -it ${Image} bash

git:
	(cd /opt/etops ; make)
