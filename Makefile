
build-dev:
	docker build .

dev:
	docker-compose up

requirements:
	pip-compile --annotate --header --generate-hashes --allow-unsafe requirements.in
	pip-compile --annotate --header --generate-hashes --allow-unsafe requirements.dev.in

upgrade:
	pip-compile --annotate --header --generate-hashes --allow-unsafe --upgrade requirements.in
	pip-compile --annotate --header --generate-hashes --allow-unsafe --upgrade requirements.dev.in

sync:
	pip-sync requirements.txt requirements.dev.txt

shell:
	docker container exec -it fineants-server_django_1 /usr/bin/zsh -i
