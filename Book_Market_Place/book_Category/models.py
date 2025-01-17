from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Categorie'
        
    def __str__(self):
        return self.name

    
class Book_Type(models.Model):
    category = models.ForeignKey(Category,related_name='book_item', on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True, null=True)
    prices = models.FloatField()
    image = models.ImageField(upload_to='photo/',blank=True ,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='book_item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.book_name
    