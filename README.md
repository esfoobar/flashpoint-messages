## Flash Messages

This app assumes denormalized input coming from somewhere external that posts city, state, username and a message.

The requirement is to get the number of cities and users that have been posted to these messages database.

I have created a post save function that would basically find the matching city, state combo and username and add to the count if it's found or create a new record in a couple of tables (UserStats and CityStats).

The processing concern here would be response time for created messages. If the influx of messages is high we could do either of two things:

   1. Make the stats update process async using something like Celery.
   2. Do a cron job that calls the sync.py file on stats_app that would go through the messages and update the counts.

The app uses sqllite for simplicity. 
   