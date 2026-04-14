python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cd my_site
python manage.py runserver