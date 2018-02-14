build:
	cd datasvc && make docker-build

run: build
	docker-compose up $(RUN_EXT) $(SERVICES)
