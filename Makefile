include env_make
NS = andrewprice
VERSION ?= latest

REPO = rps
NAME = flask
INSTANCE = default

.PHONY: build push test validate shell run start stop rm release

build:
	${INFO} "Build start"
	docker build -t $(NS)/$(REPO):$(VERSION) .
	${INFO} "Build end"

push:
	${INFO} "Push image"
	docker push $(NS)/$(REPO):$(VERSION)

test:
	${INFO} "Tests start"
	ansible-playbook deploy.yml --syntax-check
	flake8 flask_based/app.py
	flake8 flask_based/rps.py
	flake8 text_based/app.py
	pytest flask_based/
	pytest text_based/test_app.py
	${INFO} "Tests end"

validate:
	${INFO} "Validate start"
	make start
	python roles/deploy/files/validate.py
	make stop
	make rm
	${INFO} "Validate end"

shell:
	${INFO} "Container shell"
	docker run --rm --name $(NAME)_$(INSTANCE) -i -t $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) /bin/sh

run:
	${INFO} "Run Container"
	docker run --rm --name $(NAME)_$(INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

start:
	${INFO} "Start container"
	docker run -d --name $(NAME)_$(INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

stop:
	${INFO} "Stop container"
	docker stop $(NAME)_$(INSTANCE)

rm:
	${INFO} "Remove container"
	docker rm $(NAME)_$(INSTANCE)

release: build
	${INFO} "Release start"
	make push -e VERSION=$(VERSION)
	${INFO} "Release end"

default: build

# Cosmetics
YELLOW := "\e[1;33m"
NC := "\e[0m"

# Shell Functions
INFO := @bash -c '\
  printf $(YELLOW); \
  echo "=> $$1"; \
  printf $(NC)' SOME_VALUE
