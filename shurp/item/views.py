# use django decorators to ensure user is logged in
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import NewItemForm
from .models import Item

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3] #include related items in views

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items #append related items
    })

#create views for the new form
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm

@login_required
def new(request):
    form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form
    })