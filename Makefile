.PHONY: build
build:
	docker-compose -f docker-compose.yaml build

.PHONY: dev
dev:
	$(MAKE) build
	docker-compose -f docker-compose.yaml up
