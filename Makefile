.PHONY: build
build:
	docker-compose -f docker-compose.yaml build

.PHONY: dev
dev:
	$(MAKE) build
	docker-compose -f docker-compose.yaml up

.PHONY: fixtures
fixtures:
	docker-compose exec backend bash -c "python manage.py loaddata ./cards/fixtures/*"
