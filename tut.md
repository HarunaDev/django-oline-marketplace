# Build Django online market

## create virtual environment that python can work in (inside of your terminal type the command below)

virtual environment is an isolated environment in your computer where you can install python packages for your projects.

- python3 -m venv env

## to activate your virtual environment (inside of your terminal type the command below)

- source env/Scripts/activate

## to install django (inside of your terminal type the command below)

- pip install django

## to create new django project (inside of your terminal type the command below)

- django-admin startproject "project-name"

## change directory into "project-name" (inside of your terminal type the command below)

- cd "project-name"

## run django development server (inside of your terminal type the command below)

- python manage.py runserver
- then copy localhost address and paste in browser

## we will create a new django app called core (inside of your terminal type the command below)

- python manage.py startapp core

## inside of project-name/project-name/settings.py, locate INSTALLED_APPS and add 'core' to the list

## create first view in views.py

## Inside of views.py add the following python code to create a view

```python
    def index(request):
    return render(request, 'core/index.html')
```

## inside of project-name/core/ create template folder and a sub folder called core, then create a new file called index.html with html structure

## inside of urls.py import views you just created with the code below

```python
    from core.views import index, contact

    urlpatterns = [
        path('', index, name='index'),
        path('contact/', contact, name='contact'),
        path('admin/', admin.site.urls),
    ]

```
