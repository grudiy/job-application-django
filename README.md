## Django web app with submission form, other pages, admin pannel


1. pip install django 
2. django-admin startproject mysite . 
3. python manage.py startapp job_application
4. add 'job_application' to INSTALLED_APPS in settings.py
5. python manage.py runserver => to start the server and check
6. add model classes in models.py
7. python manage.py makemigrations
8. python manage.py migrate => DB is ready
9. add view functions in views.py to render views(pages)
10. create 'templates' directory with frontend templates
11. create job_apps/urls.py and add urlpatterns
12. add urlpatterns in mysite/urls.py