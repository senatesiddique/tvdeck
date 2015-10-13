from django.shortcuts import render
from django.http import HttpResponse
from tvdb.models import TVShow, Episode

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the TVDB index.")

def tvshow(request, tvshow_url_string):
	tv_show_name = tvshow_url_string.replace("-"," ").lower().title()
	return HttpResponse("You're looking at show %s." 
		% TVShow.objects.get(name=tv_show_name))

def episode(request, tvshow_id, episode_id):
    return HttpResponse(
    	"You're looking at show %s, episode %s" 
    	% (TVShow.objects.get(pk=tvshow_id),Episode.objects.get(pk=episode_id)))