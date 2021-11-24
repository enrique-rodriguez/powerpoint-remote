git clone https://github.com/enrique-rodriguez/powerpoint-remote

cd powerpoint-remote

python3 -m venv venv

source ./venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

python3 manage.py migrate --noinput

python3 manage.py collectstatic --noinput

python3 manage.py runserver 0.0.0.0:80 --insecure