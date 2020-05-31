Image=tbutzer/fluentd

build:
	docker build -t ${Image} --file Dockerfile .


push:
	docker login -u tbutzer
	docker push ${Image}


git:
	(cd /opt/etops; make)
