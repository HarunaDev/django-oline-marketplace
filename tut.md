# Build Django online market

## create virtual environment that python can work in (inside of your terminal type the command below)

virtual environment is an isolated environment in your computer where you can install python packages for your projects.

- python -m venv env

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

## create html template file with basic components that can be extended to other html files that will be created

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

Inside your django app create a new django app called items

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

## Change name of categories in django admin dashboard

Add the code snippet below to your `item/models.py`

```python
# Change the name of category
class Meta:
    ordering = ('name',)
    verbose_name_plural = 'Categories'

# Change name of categories created
def __str__(self):
    return self.name
```

## Create items model inside of `items/models.py`

Add the code snippet below to create a new class

```python
# Create items model
class Item(models.Model):
    category =  models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

Import `User` to get rid of error message

```python
from django.contrib.auth.models import User
```

## create image field and foreign key for category

Update your `Item` class in `item/models.py` with the code below

```python
category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
image = models.ImageField(upload_to='item_images', blank=True,  null=True)
```

## install pillow to handle images in app & get rid of error message

Inside of your terminal in your django app folder run the command below

```bash
pip install pillow #command one
python manage.py makemigrations #command two
python manage.py migrate #command three
```

## register item category in `admin.py`

Inside of `item/admin.py` update the existing code with the snippet below

```python
from .models import Category, Item

admin.site.register(Item)
```

## you might need to run the server again to see changes

```bash
python manage.py runserver
```

## handle media files & folders

Inside of `shurp/shurp/settings.py` add the code snippets below under `STATIC_URL = 'static/'`

```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## to view the actual name on the dashboard

Inside of `item/models.py` type in the code snippet below inside of the `Item` class

```python
def __str__(self):
        return self.name
```

## show products from the database to the front page

Inside of `shurp/core/views.py` update the function to request index page and import models with the code snippet below

```python
# import models
from item.models import Category, Item

def index(request):
    #display first 6 items in db that has not been sold
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    # request category & items
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })
```

## edit html template to display data from database

Inside `shurp/core/templates/core.index.html` update the block content with the code below

```html
<div class="mt-6 px-6 py-12 bg-gray-100 rounded-xl">
        <h2 class="mb-12 text-2xl text-center">Newest Items</h2>

        <div class="grid grid-cols-3 gap-3">
            {% for item in items %}
                <div class="">
                    <a href="#">
                        <div class="">
                            <img src="{{ item.image.url }}" class="rounded-t-xl" alt="">
                        </div>

                        <div class="p-6 bg-white rounded-b-xl">
                            <h2 class="text-2xl">
                                {{ item.name }}
                            </h2>
                            <p class="text-gray-500">Price: {{ item.price }}</p>
                        </div>
                    </a>
                </div>
            {% endfor %}
        </div>
    </div>
```

## show product images on page

Inside `shurp/shurp/urls.py` update your python script with the code below

```python
# import conf files to handle images *strictly for development
from django.conf import settings
from django.conf.urls.static import static

# update the urlpatterns list below
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## show categories and items left in front page

Inside of `templates/core/index.html` update the block content with the code below.

```html
<div class="mt-6 px-6 py-12 bg-gray-100 rounded-xl">
        <h2 class="mb-12 text-2xl text-center">Categories</h2>

        <div class="grid grid-cols-3 gap-3">
            {% for category in categories %}
            <div class="">
                <a href="#">
                    <div class="p-6 bg-white rounded-b-xl">
                        <h2 class="text-2xl">
                            {{ category.name }}
                        </h2>
                        <p class="text-gray-500">{{ category.items.count }} items</p>
                    </div>
                </a>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
```

## create & show details page

Inside of `shurp/item/views.py` add the following code to direct the user to the `details.html` or a `404` page if the item does not exist

```python
from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'item/detail.html', {
        'item': item
    })
```

Inside of `shurp/item` create a new folder `templates`, cd into `templates/` and create a new folder `item`

Change directory into `item/` and create `detail.html` and paste the code below

```html
{% extends 'core/base.html' %}

{% block title %}
{{ item.name }}
{% endblock %}

{% block content %}
<div class="grid grid-cols-5 gap-6">
    <div class="col-span-3">
        <img src="{{ item.image.url }}" alt="" class="rounded-xl">
    </div>

    <div class="col-span-2 p-6 bg-gray-100 rounded-xl">
        <h1 class="mb-6 text-3xl">{{ item.name }}</h1>
        <p class="text-gray-500"><strong>Price: </strong>{{ item.price }}</p>
        <p class="text-gray-500"><strong>Seller: </strong>{{ item.created_by.username }}</p>
        
        {% if item.description %}
            <p class="text-gray-700"><strong class="text-gray-500">Description: </strong>{{ item.description }}</p>
        {% endif %}

        <a href="#" class="inline-block mt-6 px-3 py-3 text-lg font-semibold bg-teal-500 text-white rounded-xl hover:bg-teal-700">Contact seller</a>
    </div>
</div>
{% endblock %}
```

## create urls file in `item` folder

Inside of `shurp/item` create a new file called `urls.py` to handle urls and paste the code below

```python
from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]
```

## update urls config for details page

Inside of `shurp/urls.py` update your python script with the code below

```python
# import libraries needed
from django.urls import path, include

# update the urlpatterns list with the code below
path('items/', include('item.urls')),
```

## update your index file to point to the detail url page

Inside of `core/templates/core/index.html` update the value of the `href` attribute to point to this path "{% url 'item:detail' item.id %}"

## update views to display related items in details page

Inside of `shurp/item/views.py` update the details render function with the code below

```python
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3] #include related items in views

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items #append related items
    })
```

## update details template to render related items

Inside of `shurp/item/templates/item/detail.html` update the template with the code below to show related items

```html
<div class="mt-6 px-6 py-12 bg-gray-100 rounded-xl">
    <h2 class="mb-12 text-2xl text-center">Related Items</h2>

    <div class="grid grid-cols-3 gap-3">
        {% for item in related_items %}
            <div class="">
                <a href="{% url 'item:detail' item.id %}">
                    <div class="">
                        <img src="{{ item.image.url }}" class="rounded-t-xl" alt="">
                    </div>

                    <div class="p-6 bg-white rounded-b-xl">
                        <h2 class="text-2xl">
                            {{ item.name }}
                        </h2>
                        <p class="text-gray-500">Price: {{ item.price }}</p>
                    </div>
                </a>
            </div>
        {% endfor %}
    </div>
</div>
```

## Signing Up

## Create new `urls.py` file to handle user sign-up

Inside of `shurp/core` create a new `urls.py` file and paste the code below to handle url configurations

```python
# urls.py file to handle signing up

# import neccessary modules
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name='contact')
]
```

## Update the urls config file in `shurp/shurp/`

Inside of `shurp/shurp/urls.py` update the code there with the snippet below change the line that is importing views module and the first item in the `url` patterns list. 

```python
from core.views import about, privacy, terms

urlpatterns = [
    path('', include('core.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### Bug 🐛

Inside of `shurp/core/templates/core/base.html` update the contact url at the footer with the code below

```html
<li><a href="{% url 'core:contact' %}" class="text-lg text-teal-500 hover:text-teal-700">Contact</a></li>
```

## Create `forms.py` file to handle sign-up and login validation.

Inside `shurp/core/` create a new file `forms.py` and paste the code snippet below.

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
```

## Create models for users and fields that they are required to fill

Below the import statements in the `forms.py` files paste the code below

```python
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
```

## Update views to display signup form

Inside of `shurp/core/views.py` update your code with the snippet below

```python
# create view for signup form
from .forms import SignupForm

def signup(request):
    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
```

## Create `signup.html` template to display form

Inside of `shurp/core/templates/core` create `signup.html` and paste the code snippet below

```html
{% extends 'core/base.html' %}

{% block title %} Sign Up {% endblock %}

{% block content %}
<div class="w-1/2 my-6 mx-auto p-6 bg-gray-100 rounded-xl">
    <h1 class="mb-6 text-3xl">Sign Up</h1>

    <!-- add form -->
    <form method="post" action=".">
        {% csrf_token %}

        <button class="py-4 px-8 text-lg bg-teal-500 hover:bg-teal-700 rounded-xl text-white">Submit</button>
    </form>

</div>
{% endblock %}
```

## Update `urls.py` to direct users to signup page

Inside of `shurp/core/urls.py` update the `urlpattern` list with this line of code `path('signup/', views.signup, name="signup")`

## Update `signup.html` with form fields

Inside of `shurp/core/templates/core/signup.html` update the form section with the code below

```html
<!-- add form -->
    <form method="post" action=".">
        {% csrf_token %}

        <div class="mb-3">
            <label for="" class="inline-block mb-2">Username</label> <br>
            {{ form.username }}
        </div>

        <div class="mb-3">
            <label for="" class="inline-block mb-2">E-mail</label> <br>
            {{ form.email }}
        </div>

        <div class="mb-3">
            <label for="" class="inline-block mb-2">Enter Password</label> <br>
            {{ form.password1 }}
        </div>

        <div class="mb-3">
            <label for="" class="inline-block mb-2">Enter Password again</label> <br>
            {{ form.password2 }}
        </div>

        {% if form.errors or form.non_field_errors %}
            <div class="mb-3 p-6 bg-red-100 rounded-xl">
                {% for field in form %}
                    {{ field.errors }}
                {% endfor %}

                {{ form.non_field_errors }} <!-- errors not connected to form field -->
            </div>
        {% endif %}

        <button class="py-4 px-8 text-lg bg-teal-500 hover:bg-teal-700 rounded-xl text-white">Submit</button>
    </form>
```

## Create styles for form in `forms.py`

Inside of `shurp/core/forms.py` update the `SignupForm` class with the code below

```python
username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': 'w-full py-4 px-6 rounded-xl'
}))

email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Your email address',
    'class': 'w-full py-4 px-6 rounded-xl'
}))

password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Your password',
    'class': 'w-full py-4 px-6 rounded-xl'
}))

password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Repeat password',
    'class': 'w-full py-4 px-6 rounded-xl'
}))
```

## Validate user authentication and redirect to login

Inside of `shurp/core/views.py` update the code to validate user auth and redirect user to login page

```python
# validate form before creating user
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form = SignupForm()
```

Also import `redirect` at the top of your script

## Create a template for login page

Inside of `shurp/core/templates/core/` create a `login.html` file and extend some elements

```html
{% extends 'core/base.html' %}

{% block title %}
    Login
{% endblock %}

{% block content %}
    <h1>The Login page..</h1>
{% endblock %}
```

## Update `views.py` to render login template

Inside of `shurp/core/views.py` add the block of code below

```python
def login(request):
    return render(request, 'core/login.html')
```

## Update URL patterns list

Inside of `shurp/core/urls.py` update the url patterns list with the code below

```python
urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login")
]
```

## vyond for video editing

## Create Login class to handle User login

Inside of `shurp/core/forms.py` create a login class that takes username and password

```python
# create login form class
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
```

Don't forget to include `AuthenticationForm` among your imports atthe top of the script

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
```

## Update url patterns to direct users to django login form

Inside of `shurp/core/urls.py` update your code with the snippet below

```python
# urls.py file to handle signing up
from django.contrib.auth import views as auth_views

# import neccessary modules
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login')
]
```

## update login button link in `base.html`

Inside of `shurp/core/templates/core/base.html` update the `href` value of the login link with this value `{% url 'core:login' %}`

## update url pattern to display login template

Inside of `shurp/core/urls.py` update the url patterns with the code below

```python
urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login')
]
```

## update login template

Inside of `shurp/core/templates/core/login.html` update the template page with the code below

```html
{% extends 'core/base.html' %}

{% block title %} Login {% endblock %}

{% block content %}
<div class="w-1/2 my-6 mx-auto p-6 bg-gray-100 rounded-xl">
    <h1 class="mb-6 text-3xl">Login</h1>

    <!-- add form -->
    <form method="post" action=".">
        {% csrf_token %}

        <div class="mb-3">
            <label for="" class="inline-block mb-2">Username</label> <br>
            {{ form.username }}
        </div>

        <div class="mb-3">
            <label for="" class="inline-block mb-2">Enter Password</label> <br>
            {{ form.password }}
        </div>

        {% if form.errors or form.non_field_errors %}
            <div class="mb-3 p-6 bg-red-100 rounded-xl">
                {% for field in form %}
                    {{ field.errors }}
                {% endfor %}

                {{ form.non_field_errors }} <!-- errors not connected to form field -->
            </div>
        {% endif %}

        <button class="py-4 px-8 text-lg bg-teal-500 hover:bg-teal-700 rounded-xl text-white">Submit</button>
    </form>

</div>
{% endblock %}
```

## Create login redirect routes for logged out users and users who login

Inside of `shurp/shurp/settings.py` paste the code below

```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

## Update `base.html` to hide buttons when a user is logged in

Inside of `shurp/core/templates/core/base.html` update the code that displays the signup and login buttons with the code below

```html
<!-- show buttons if user is signed in -->
            {% if request.user.is_authenticated %}
            {% else %}
                <a href="{% url 'core:signup' %}" class="px-6 py-3 text-lg font-semibold bg-teal-500 text-white rounded-xl hover:bg-teal-700">Sign up</a>

                <a href="{% url 'core:login' %}" class="px-6 py-3 text-lg font-semibold bg-gray-500 text-white rounded-xl hover:bg-gray-700">Login up</a>
            {% endif %}
```

## Add dashboard and message buttons in navbar

Inside of `shurp/core/templates/core/base.html` update the navbar section with the code below

```html
<a href="#" class="px-6 py-3 text-lg font-semibold bg-teal-500 text-white rounded-xl hover:bg-teal-700">Dashboard</a>

<a href="#" class="px-6 py-3 text-lg font-semibold bg-gray-500 text-white rounded-xl hover:bg-gray-700">Message</a>

```