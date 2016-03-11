from django.db import models

class CityStats(models.Model):
    state = models.CharField('State', db_index=True, max_length=64)
    city = models.CharField('City', db_index=True, max_length=64)
    quantity = models.IntegerField()
    
class UserStats(models.Model):
    username = models.CharField('User', db_index=True, max_length=64)
    quantity = models.IntegerField()