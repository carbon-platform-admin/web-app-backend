from django.db import models

# Create your models here.



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=40)
    carbon_footprint_score = models.DecimalField(max_digits=6, decimal_places=2)
    account_type = models.CharField(max_length=10, default="Free")
    profile_picture = models.FileField(upload_to="profile_pictures/", null=True, blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    