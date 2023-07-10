rd /s /q "venv"
py -m venv venv
.\venv\Scripts\activate   
pip install -r requirements.txt 
python .\netplas\manage.py migrate --run-syncdb
python .\netplas\manage.py createsuperuser
@REM python .\netplas\manage.py runserver 