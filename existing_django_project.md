# How to set up a cloned Django project

![Django clone setup](./img/django_clone.jpg)

## In this article, you will learn how to set up a cloned Django project on your computer

## This article is easy to follow even if you don't have experience working with Django or Git

When working on a Django project with git, developers will likely want git to ignore some files and folders. The `env/` folder in your Django project is one of those folders that git should ignore.

The `env/` folder is used to isolate project-specific dependencies, and manage Python packages.

Cloning such projects into your PC will require you to set up a virtual environment on your computer to manage some dependencies that the project needs.

Cloning a Django project can be confusing sometimes, especially for a Python developer who is new to Django.

Below are step-by-step guides on how to solve this problem.

1. Clone the project

```bash
    git clone https://github.com/<username>/<project-name>.git
```

2. Change directory into cloned project

```bash
    cd <project-name>/
```

3. Create virtual environment to manage dependencies

```bash
    Python -m venv env && source env/Scripts/actiivate
```

The commands above will create and activate a virtual environment on your machine. The virtual environment will store all the required dependencies that your project needs.



4. Install Python packages needed for project

```bash
    pip install <package1> <package2> <package3>
```

`pip install` is used to install Python packages into your project. An example of such a package is `Django`.

5. Change directory into Django App

```bash
    cd <django-app-name>
```

6. Run Django project in server

```bash
    python manage.py runserver
```

After running the command above, hold `ctrl` on your 
keyboard and click on the local host link in your terminal to view your application in your browser. 