1.Environment
		
    pip install pipenv
    pipenv shell (inside project folder)(create or activate env)
----------------------------------------------
2.Libraries

    pipenv install pillow for working with image 
    pipenv install django
----------------------------------------------
3.Start Project 

    django-admin startproject stayWatch
----------------------------------------------
4.Database setup (MySQL)

    pipenv install mysqlclient
    In MySQL command line client
    CREATE DATABASE STAYWATCH;
    USE STAYWATCH;

    In django > stayWatch > settings.py 
    edit DATABASES as:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'staywatch',
            'USER': 'root',
            'PASSWORD': '1234',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    python manage.py makemigrations
    python manage.py migrate

    in mysql cmd > show tables;
    +----------------------------+
    | Tables_in_staywatch        |
    +----------------------------+
    | auth_group                 |
    | auth_group_permissions     |
    | auth_permission            |
    | auth_user                  |
    | auth_user_groups           |
    | auth_user_user_permissions |
    | django_admin_log           |
    | django_content_type        |
    | django_migrations          |
    | django_session             |
    +----------------------------+
----------------------------------------------
5. Run the project

    python manage.py runserver
----------------------------------------------
6 Adding an Admin Panel
    
    create SU
        python manage.py createsuperuser
        username: user
        password: 1234
    
    goto: http://127.0.0.1:8000/admin/login/?next=/admin/

----------------------------------------------
7 


