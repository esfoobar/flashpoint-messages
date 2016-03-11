from django.db import models

from stats_app.models import CityStats, UserStats

class Messages(models.Model):
    state = models.CharField('State', db_index=True, max_length=64)
    city = models.CharField('City', db_index=True, max_length=64)
    username = models.CharField('User', db_index=True, max_length=64)
    message = models.TextField('Message')
    create_time = models.DateTimeField('Date', db_index=True, auto_now_add=True) 

    class Meta:
        ordering = ['state', 'city', 'create_time']

    def save(self, *args, **kwargs):
            super(Messages, self).save(*args, **kwargs)
            self.increment_count(self.city, self.username)
            
    def increment_count(self):
        try:
            target_city = CityStats.objects.get(city=self.city)
            target_city.quantity += 1
            target_city.save()
        except CityStats.DoesNotExist:
            CityStats(city=self.city, quantity=1).save()
        try:
            target_user = UserStats.objects.get(username=self.username)
            target_user.quantity += 1
            target_user.save()
        except UserStats.DoesNotExist:
            UserStats(username=self.username, quantity=1).save()
            
        
        