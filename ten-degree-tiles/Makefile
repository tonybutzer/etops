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
	echo please cd into runs/$${RUNN} and run -- make model_prepare; \
	echo I SAID PLEASE cd runs/$${RUNN} -- and run -- make model_prepare
