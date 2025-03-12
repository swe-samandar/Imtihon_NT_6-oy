from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=200) 
    district = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    floor = models.PositiveSmallIntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=2)    
    rooms = models.PositiveIntegerField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_new = models.BooleanField(default=False)
    image = models.ImageField(upload_to='houses/', blank=True, null=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'house'

    def __str__(self):
        return f"{self.city} shahar, {self.district} tuman, {self.company} MChJ"