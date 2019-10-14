tests:
	docker-compose down
	docker-compose run --rm test

run_local:
	docker-compose down
	docker-compose up web

circle_ci_local:
	circleci local execute 