from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tvshow_url_string>[\w\W]+)/$', views.tvshow, name='tvshow'),
    url(r'^(?P<tvshow_id>[0-9]+)/(?P<episode_id>[0-9]+)$', views.episode, name='episode'),
]