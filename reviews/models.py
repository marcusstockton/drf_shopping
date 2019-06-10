from django.db import models
from django.contrib.auth.models import User
from items.models import Item
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')

    def __repr__(self):
        return '<Review %s>' % self.title

    def __str__(self):
        return self.title