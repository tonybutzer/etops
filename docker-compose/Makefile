info:
	echo hello cube in the box testors

up:
	docker-compose up -d 

down:
	docker-compose down

exec:
	docker-compose exec debug bash
test_logging:
	docker run --log-driver=fluentd --log-opt tag="docker.{{.Name}}" ubuntu echo 'Hello Fluentd!'

git:
	(cd /opt/etops; make)

upgrade:
	sudo curl -L https://github.com/docker/compose/releases/download/1.25.0-rc4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose


debug:
	#docker network create somenetwork
	#docker run -d --memory=4g --memory-swap=-1 --name elasticsearch --net somenetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.4.0
	docker run -d --memory=4g --memory-swap=-1 --name elasticsearch --net somenetwork -p 9200:9200 -p 9300:9300 -e ES_JAVA_OPTS="-Xms512m -Xmx512m" docker.elastic.co/elasticsearch/elasticsearch:7.4.0


memory:
	sudo docker info
	sudo echo 'GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1' >> /etc/default/grub
	sudo update-grub
	sudo docker info

# Changes will take effect when the system is rebooted. Confirm that changes have taken effect by again running the following command

test_memory:
	sudo docker run -it --memory=2g --memory-swap=2g ubuntu /bin/bash

