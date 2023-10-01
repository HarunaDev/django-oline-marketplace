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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>shurp</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <div class="px-6 py-6">
        <h1>The front page</h1>
    </div>
</body>
</html>
```

## inside of urls.py import views you just created with the code below

```python
    from core.views import index

    urlpatterns = [
        path('', index, name='index'),
        path('admin/', admin.site.urls),
    ]

```

## create html template file with basic components that can be extended to other html files that will be created. 

inside of templates\core create a new html file (base.html) and paste the code below

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} {% endblock %} | shurp</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <div class="px-6 py-6">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```

## inside of your index.html replace the existing code with the one below

```html
{% extends 'core/base.html' %}

{% block title %}
    Welcome
{% endblock %}

{% block content %}
    <h1>The front page..</h1>
{% endblock %}
```

## Challenge 

Create a new contact page that extends from the base.html

Remember to update your views.py and urls.py file

## Solution

First we need to create a new file in templates\core (contact.html) and paste the code below

```html
{% extends 'core.base.html' %}

{% block title %}
    Contact
{% end block %}

{% block content %}
    The contact page
{% end block %}

```

We update your views.py with the code below to render out the contact page. 

```python
def contact(request):
    return render(request, 'core/contact.html')    
```

Now update your urls.py with the code below

```python
from core.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]
```