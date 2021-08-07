![https://img.shields.io/badge/<Django>-<v3.2.6>-<blue>]


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
7. Add path to templates folder
    settings.py > TEMPLATES > 'DIRS': ['templates']
    Create directory 'templates' in main project folder

----------------------------------------------
 8. Serving static files
    
    all css,js,assets files stored in staticFiles

    for deployment purpose use : https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/
    otherwise:
        STATIC_URL has the url from where the static files are served
        in settings.py 
STATIC_ROOT = os.path.join(BASE_DIR,'static')

            STATIC_ROOT = os.path.join(BASE_DIR,'static')

            STATICFILES_DIRS = [
                add paths to your static files here for ex: os.path.join(BASE_DIR,'appName/staticFolderName')
            ]

        django will search all these folder to find static files and move them to a new folder called static to serve to client

        Run: python manage.py collectstatic
----------------------------------------------
9. Create an app webpages
    python manage.py startapp webpages

    creates an app named webpages with app name 'WebpagesConfig'
    add urls.py file to webpages app

    settings.py >
    add 'webpages.apps.WebpagesConfig' to INSTALLED_APPS
----------------------------------------------



