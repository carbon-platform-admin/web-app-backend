from django.db import models

# Create your models here.
from categories.models import Category
class Blog(models.Model):
    BLOG_TYPES = (
        ('V', 'Vlog'),
        ('B', 'Blog'),
        ('A', 'Article')
    )
    
    title = models.CharField(max_length=100)
    blog_type = models.CharField(max_length=20, choices=BLOG_TYPES)
    
    content = models.TextField(blank=True, null=True)
    
    external_link = models.URLField(null=True, blank=True)
    
    thumbnail = models.URLField(null=True, blank=True)
    
    timestamp = models.DateTimeField(auto_now=True)
    
    category = models.ForeignKey(Category, max_length=40, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    