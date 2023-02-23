from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=75)

    icon_url = models.URLField(null=True, blank=True)
    
    icon_alt_text = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.name
