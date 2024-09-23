# use django decorators to ensure user is logged in
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import Item, Category
from django.db.models import Q

# Create your views here.
# create view for browse
def items(request):
    # get query and pass it to frontend
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    # check if query is filled and if it is in items
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
    })

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
    # check if method is post then get and validate files before saving to database
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False) #save files in object before storing in database
            item.created_by = request.user # get the created by data and save to user before saving the files to database
            item.save()

            return redirect('item:detail', pk=item.id)
    else: #else if it is a get request, we just render the new item form
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })

# check if user is logged in before granting access to edit item
@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    # check if method is post then get and validate files before saving to database
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else: #else if it is a get request, we just render the new item form
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item',
    })

# delete item view
@login_required
def delete(request, pk):
    # get items created by the authenticated user before deleting
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')