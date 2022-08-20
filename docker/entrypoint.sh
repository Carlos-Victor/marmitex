#!/bin/sh
set -e

run_migrations() {
    python manage.py migrate
}

until pg_isready --host=$DB_HOST --port=$DB_PORT --dbname=$DB_NAME --username=$DB_USER
do
    echo "Aguardando PostgresSQL"
    sleep 3;
done
echo "PosgresSQL está pronto para receber conexão!"


if [ "$1" = "debug" ]; then
    exec tail -f /dev/null

elif [ "$1" = "local" ]; then
    run_migrations &&
    exec python manage.py runserver 0.0.0.0:8000

else
    exec gunicorn -b 0.0.0.0:8000 marmitex.wsgi -w 3 --timeout 0 wsgi
fi
