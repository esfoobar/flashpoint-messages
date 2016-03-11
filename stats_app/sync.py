import os, sys
from django.core.wsgi import get_wsgi_application
proj_path = "/home/ubuntu/workspace/flashmessages/flashmessages"
sys.path.append(proj_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flashmessages.settings")
application = get_wsgi_application()

from messages_app.models import Messages
from stats_app.models import CityStats, UserStats

# wipe stats
CityStats.objects.all().delete()
UserStats.objects.all().delete()

# get all messages
messages = Messages.objects.all()

for message in messages:
    message.increment_count()
    
    