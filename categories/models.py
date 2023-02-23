from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    
    # Icon for the category
    icon_url = models.URLField(null=True, blank=True)
    
    # Promotional text
    
    promotional_text = models.TextField(null=True, blank=True)
    
    # Icon background color
    bg_color = models.CharField(max_length=7, null=True, blank=True)
    # Larger image used for the category
    image_url = models.URLField(null=True, blank=True)
    
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="children")
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    