from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # odering = ('name',) // check for error on this line
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name