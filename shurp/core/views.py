from django.shortcuts import render, redirect

# import models
from item.models import Category, Item

# create view for signup form
from .forms import SignupForm

# Create your views here.
def index(request):
    #display first 6 items in db that has not been sold
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    # request category & items
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def terms(request):
    return render(request, 'core/terms.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def signup(request):
    # validate form before creating user
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })