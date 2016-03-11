from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get$', views.stats_get, name='stats_get'),
]