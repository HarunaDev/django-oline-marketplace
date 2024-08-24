# use django decorators to ensure user is logged in
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import NewItemForm
from .models import Item

# Create your views here.
# create view for each detail of an item
def detail(request, pk):
    # get detail of item from database and also related items from the same category
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3] #include related items in views

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items #append related items
    })

# check if user is logged in before granting access to add new item
@login_required
def new(request):
    form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })