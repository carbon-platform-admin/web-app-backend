from django.db import models

from products.models import Product

# Create your models here.
class Review(models.Model):
    user = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    title = models.CharField(max_length=40)
    
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title