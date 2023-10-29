# doradca
Web application to manage law office

## docker
docker-compose run --rm app sh -c "python manage.py test -v 2"

docker-compose run app sh -c "python manage.py makemigrations"

docker volume ls
docker volume rm krg_currencies_dev-db-data
docker volume prun

docker-compose up