from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    location = models.CharField(max_length=100)
    size = models.IntegerField(default=0)
    area_sqft = models.FloatField(default=0.0)
    bath = models.FloatField(default=0.0)
    balcony = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.location} and price: {self.price}"
