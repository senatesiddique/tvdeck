from django.db import models

# Create your models here.
class TVShow(models.Model): 
	name = models.CharField(max_length=100)
	start_date = models.DateField()
	end_date = models.DateField()
	rating = models.DecimalField(max_digits=4, decimal_places=2)
	poster = models.ImageField(upload_to='tvdb\static\posters')

	def _get_url_string(self):
		"URL Encode of show name"
		return self.name.replace(" ", "-")

	url_string = property(_get_url_string)

	def _get_total_runtime(self):
		"Sum of episode runtimes"
		return TVShow.objects.aggregate(total_runtime=models.Sum('episode__runtime'))
	
	total_runtime = property(_get_total_runtime)

	def _get_average_episode_rating(self):
		"Average of episode ratings"
		return TVShow.objects.aggregate(avg_episode_rating=models.Avg('episode__rating'))

	avg_episode_rating = property(_get_average_episode_rating)

	def __str__(self): 
		return self.name

class Episode(models.Model):
	tv_show = models.ForeignKey('TVShow')
	season = models.IntegerField()
	episode_number = models.IntegerField()
	name = models.CharField(max_length=100)
	air_date = models.DateField()
	runtime = models.IntegerField()
	rating = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self): 
		return self.name