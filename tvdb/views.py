from django.shortcuts import render
from django.http import HttpResponse
from tvdb.models import TVShow, Episode, Season

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the TVDB index.")

def tvshow(request, tvshow_url_string):
	tv_show_name = tvshow_url_string.replace("-"," ").lower().title()
	return HttpResponse("You're looking at show %s." 
		% TVShow.objects.get(name=tv_show_name))

def season(request, tvshow_url_string, season_url_string):
	tv_show_name = tvshow_url_string.replace("-"," ").lower().title()
	season_number = int(season_url_string.replace("s",""))
	season = Season.objects.get(tv_show__name=tv_show_name,season_number=season_number)
	return HttpResponse("You're looking at show %s, season %s." 
		% (TVShow.objects.get(name=tv_show_name), season))

def episode(request, tvshow_url_string, season_url_string, episode_url_string):
	tv_show_name = tvshow_url_string.replace("-"," ").lower().title()
	season_number = int(season_url_string.replace("s",""))
	episode_number = int(episode_url_string.replace("e",""))
	season = Season.objects.get(tv_show__name=tv_show_name,season_number=season_number)
	episode = Episode.objects.get(tv_show__name=tv_show_name,episode_number=episode_number)
	return HttpResponse(
    	"You're looking at show %s, episode %s" 
    	% (TVShow.objects.get(name=tv_show_name),episode))
