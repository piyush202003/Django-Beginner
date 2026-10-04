a)temporary:Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
b)permanent:Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

gunicorn myproject.wsgi:application
uvicorn myproject.asgi:application

.venv\Scripts\activate
while install use command :- uv pip install PACKEGNAME
python version 3.10 :- uv python install 3.10

to list all the requirement in .txt file :- uv pip freeze > requirements.txt

in vs code add emmet language:- key= django-html, value=html

to add tailwind:-
    1. add 'tailwind' in setting-> app
    2. run command:- python manage.py tailwind init
        then give theme name and add it also in setting-> app
        also add veriables:- 
            TAILWIND_APP_NAME='theme'
            INTERNAL_IPS=['127.0.0.1']
            NPM_BIN_PATH = r"\\usr\\local\\bin\\npm"
            to get npm path in windows :- where.exe npm
    3. Then run this command:- python manage.py tailwind install 
    4. keep running this command on other terminal:- python manage.py tailwind start
    5. for deployment use command :- python manage.py tailwind build

to add reload:
    1. add 'django_browser_reload' in setting->app
    2. in middlware add:- django_browser_reload.middleware.BrowserReloadMiddleware
    3. now in urls.py file add this path:- path("__reload__/",include("django_browser_reload.urls"))

to start images:
    1. import os
    2. MEDIA_URL = '/media/'
    3. MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    4. now in urls.py file:-
        from django.conf import settings
        from django.conf.urls.static import static
        urlspattern = [

        ]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

to load static files like .css:
    1. import os
    2. STATICFILES_DIRS = [os.path.join( BASE_DIR , 'static' )]

to use django REST API framework:
    1. uv pip install djangorestframework
    2. add 'rest_framework' in installed apps in settings.py
    2. don't need to set this in the setting:- also add this in setting.py file:- 
        REST_FRAMEWORK = {
            # Use Django's standard `django.contrib.auth` permissions,
            # or allow read-only access for unauthenticated users.
            'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
            ]
        }   

