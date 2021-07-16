from django.db import models
from django.urls import reverse
# Create your models here.

class Card(models.Model):
    value = models.IntegerField()
    category = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return (f"{self.value} of {self.category}")

    def get_url(self):
        return reverse('play',args=[self.id])