from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __repr__(self):
        return '<Item %s>' % self.title

    def __str__(self):
        return self.title
