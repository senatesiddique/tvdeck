from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tvdeck.views.home', name='home'),
    url(r'^', include('tvdb.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
