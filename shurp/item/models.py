#import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

## create category class that takes name input
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',) #bug was a typo 🤣 
        verbose_name_plural = 'Categories'
    
    # displays the name of the category on dashboard
    def __str__(self):
        return self.name

# Create items model to get details of an item that should be stored in a database
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True,  null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # displays the name of the item on the dashboard
    def __str__(self):
        return self.name
