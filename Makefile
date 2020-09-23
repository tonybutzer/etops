cloud_et_for_dummys:
	@echo "What is your age?: "; \
	read AGE; \
	echo "Your age is " $${AGE}
	@echo How dumb can you really be?
	@echo "What is the name of this run? example drb40yr: "; \
        read RUNN; \
        echo "Your run name is " $${RUNN}; \
	echo "FIXING THE MAKEFILE ..." ; \
	cp -r ./veget_docker_gold_image_c runs/$${RUNN} ; \
	sed -i s/RUNN/$${RUNN}/g runs/$${RUNN}/Makefile; \
	sed -i s/RUNN/$${RUNN}/g runs/$${RUNN}/Dockerfile; \
	echo please cd into runs/$${RUNN} and run -- make model_prepare
	echo I SAID PLEASE cd runs/$${RUNN} -- and run -- make model_prepare

publish:
	git remote set-url origin git@github.com:tonybutzer/etops.git
	#git remote set-url origin https://github.com/tonybutzer/etops.git
	git config --global user.email tonybutzer@gmail.com
	git config --global user.name tonybutzer
	git config --global push.default simple
	git add .
	git commit -m "automatic git update from Makefile"
	git push


docker-enable:
	#sudo groupadd docker
	sudo usermod -aG docker ubuntu
