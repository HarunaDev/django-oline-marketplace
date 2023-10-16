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

## add nav bar to app

Update your base.html with the code below

```html
    <!-- add nav element inside of your body tag -->
    <nav class="py-6 px-6 flex justify-between items-center border-b border-gray-200">
        <a href="/" class="text-xl font-semibold">Puddle</a>

        <div class="space-x-6">
            <a href="#" class="text-lg font-semibold hover:text-gray-500">New item</a>
            <a href="#" class="text-lg font-semibold hover:text-gray-500">Browse</a>

            <a href="#" class="px-6 py-3 text-lg font-semibold bg-teal-500 text-white rounded-xl hover:bg-teal-700">Sign up</a>

            <a href="#" class="px-6 py-3 text-lg font-semibold bg-gray-500 text-white rounded-xl hover:bg-gray-700">Login up</a>
        </div>
    </nav>
```

## add footer to app

Inside of your base.html file add the code below to the end of your body tag

```html
    <footer class="py-6 px-6 flex justify-between bg-gray-800">
        <div class="w-2/3 pr-10">
            <h3 class="mb-5 font-semibold text-gray-400">About</h3>

            <p class="text-lg text-gray-500">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore distinctio aspernatur dolorem, sunt explicabo quas.
            </p>
        </div>

        <div class="w-1/3">
            <h3 class="mb-5 font-semibold text-gray-400">Menu</h3>

            <ul class="space-y-2">
                <li><a href="#" class="text-lg text-teal-500 hover:text-teal-700">About</a></li>
                <li><a href="#" class="text-lg text-teal-500 hover:text-teal-700">Contact</a></li>
                <li><a href="#" class="text-lg text-teal-500 hover:text-teal-700">Privacy</a></li>
                <li><a href="#" class="text-lg text-teal-500 hover:text-teal-700">Terms of use</a></li>
            </ul>
        </div>
    </footer>
```

## how to jump to a link or a new view in django

Inside of your base.html update your contact link item with the code below

```html
<li><a href="{% url 'contact' %}" class="text-lg text-teal-500 hover:text-teal-700">Contact</a></li>
```

## how to add categories and items to app


Inside your <django app> create a new django app called items

```bash
python manage.py startapp item
```

## inside of settings.py, locate INSTALLED_APPS and add 'item' to the list

## create database model

Inside of `items/` add the code below to the `models.py` file

```python
class Category(models.Model):
    name = models.CharField(max_length=255)
```
Run the following commands in your command line to create categories and execute script

```bash
python manage.py makemigrations && python manage.py migrate
```

## create user in admin to be able to add items to categories

```bash
python manage.py createsuperuser
## fill in the details
```

## runserver and visit `<django app url>/admin` to login your 

## import and register models inside `item/admin.py` 

```python
# Import models
from .models import Category

# Register your models here.
admin.site.register(Category)
```