from django.test import TestCase

from messages_app.models import Messages
from stats_app.models import CityStats, UserStats

class MessageStatsTestCase(TestCase):
    def setUp(self):
        Messages.objects.create(state="NY", city="New York", username="larry74", message="Testing")
        Messages.objects.create(state="NY", city="New York", username="bob88", message="Testing")
        Messages.objects.create(state="NY", city="Brooklyn", username="larry74", message="Testing")
        Messages.objects.create(state="CA", city="San Francisco", username="john22", message="Testing")
        Messages.objects.create(state="GA", city="Athens", username="john22", message="Testing")
        Messages.objects.create(state="NY", city="Athens", username="john22", message="Testing")

    def test_city_stats(self):
        num_cities = CityStats.objects.all().count()
        num_users = UserStats.objects.all().count()
        self.assertEqual(num_cities, 5)
        self.assertEqual(num_users, 3)
