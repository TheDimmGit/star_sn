echo "Running migrations"
python manage.py makemigrations --no-input
python manage.py migrate --no-input

echo "Running server"
python manage.py runserver 0.0.0.0:8000
