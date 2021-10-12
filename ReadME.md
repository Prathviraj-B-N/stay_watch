![Framework](https://img.shields.io/badge/Django-3.2.6-blue)



![Screenshot](https://github.com/Prathviraj-B-N/stay_watch/blob/ef8b955b8c8a8b83a5c1e3f25fd271a554d5f6b4/stayWatch/Capture.JPG)




----------------------------------------------


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
9. Create an app 'webpages'
    
        python manage.py startapp webpages

        creates an app named webpages with app name 'WebpagesConfig'
        add urls.py file to webpages app

        settings.py >
        add 'webpages.apps.WebpagesConfig' to INSTALLED_APPS
----------------------------------------------
10. Setting up urls.py in main project folder(project level urls.py)

        from django.urls import include
        from django.conf.urls.static import static
        
        1.add this to urlpatterns so that we can define app level urls.py
            path('',include('webpages.urls'))

        2.add static root to urlpatterns
            urlspattern += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 
----------------------------------------------
11. Setting up urls.py in app level

        for each view, setup root
        ex: path('',views.home,name = "home")
----------------------------------------------
12. Setting up views.py
        
        def home(request):
            pass
----------------------------------------------
13. Templating
        define base.html in templates
        in all other files use 
            {% extends 'base.html' %}
            {% block content %}
            {% endblock %}

        {% include 'htmlSnippet.html' %}
----------------------------------------------
14. Add your static files like js,css into staticFiles foder

        python manage.py collectstatic
        in html files add {% load static %}
----------------------------------------------
15. Setup paths for css and js in html files

        {% static "css/filename.css" %} by default searches in static
----------------------------------------------
16. Model the data
    
        webpages>>models.py
        after modelling register it in admin.py
            python manage.py makemigrations
            python manage.py migrate
----------------------------------------------
17. Access data from webpage

        in views.py import model
        query data 
        pass it to render method
        to add photo to html : {{ obj.photo.url }}
----------------------------------------------
18. To add user defined filter to use in jinja templating

    (used this to implement rating system)
        
        1.create templatetags directory in app level
            a.create filter.py
            bregister your filter in it
        2.in settings.py
            a.register filter.py in registered apps

            b.add
                libraries':{
                    'filter': 'webpages.templatetags.my_filters',
                },

            to templates>options

19. href = {% url 'name' %} here name is the name you have assigned to url in urls.py

20. pipenv install django-ckeditor

21. in admin.py you can edit admin panel look 
        you can add search fields etc to admin panel by defining a class
            ex: class StayAdmin(admin.ModelAdmin):
    
22. User Auth
        Create a new app for auth lets call it stayAuth




     







