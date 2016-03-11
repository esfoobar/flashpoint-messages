from django.db import models

class CityStats(models.Model):
    city = models.CharField('City', db_index=True, max_length=64)
    quantity = models.IntegerField()
    
class UserStats(models.Model):
    username = models.CharField('User', db_index=True, max_length=64)
    quantity = models.IntegerField()