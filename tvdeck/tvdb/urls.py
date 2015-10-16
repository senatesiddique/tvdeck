from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tvshow_url_string>[\w\W]+)/(?P<season_url_string>[s0-9]+)/(?P<episode_url_string>[e0-9]+)/$', 
    	views.episode, name='episode'),
    url(r'^(?P<tvshow_url_string>[\w\W]+)/(?P<season_url_string>[s0-9]+)/$', 
    	views.season, name='season'),
    url(r'^(?P<tvshow_url_string>[\w\W]+)/$', views.tvshow, name='tvshow'),
]