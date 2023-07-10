# MRP-Project-System-Analysis--Lesson

We created MRP (Material Requirements Planning) API. We used Django and DRF. 


## Installation
Clone the repository and create a virtual environment.

    $ git clone https://github.com/umit-ozturk/MRP-Project-System-Analysis--Lesson.git
	$ cd MRP-Project-System-Analysis--Lesson
	$ virtualenv -p python3 env
	$ source env/bin/activate
    $ pip install -r requirements.txt
    $ cd netplas


## Create user
    $ python manage.py migrate
    $ python manage.py createsuperuser

    
If you have no such table error ( Use PostgreSQL. You don't have local settings Project uses SQLite by default. )

    $ python manage.py migrate --run-syncdb
    $ python manage.py createsuperuser
    
## Run Server
    
    $ python manage.py runserver
