from django.contrib import admin

from .models import TVShow, Episode, Season

# Register your models here.
class TVShowAdmin(admin.ModelAdmin):
    fields = ['name','start_date','end_date','rating','poster','url-string']

class EpisodeAdmin(admin.ModelAdmin):
    fields = ['tv_show','season','name','air_date','rating','runtime','episode_number']

class SeasonAdmin(admin.ModelAdmin):
    fields = ['tv_show','season_number']

admin.site.register(TVShow, TVShowAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Episode, EpisodeAdmin)