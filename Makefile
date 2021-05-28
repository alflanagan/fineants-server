
build-dev:
	docker build .

dev:
	docker-compose up

requirements:
	pip-compile --annotate --header --generate-hashes --reuse-hashes --allow-unsafe requirements.in
	pip-compile --annotate --header --generate-hashes --reuse-hashes --allow-unsafe requirements.dev.in

sync:
	pip-sync requirements.txt requirements.dev.txt
