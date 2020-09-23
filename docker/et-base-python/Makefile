Image=tbutzer/et-base-python

build:
	docker build -t ${Image} .

run:
	docker run -it ${Image} bash

exec:
	docker exec -it ${Image} bash

dockerhub_publish:
	(docker login && docker push ${Image})

