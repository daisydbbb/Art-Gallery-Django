from django.db import models

class Collection(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  art_name =  models.CharField(max_length=100)
  artist_name = models.CharField(max_length=50)
  artist_country = models.CharField(max_length=50)
  year_created = models.CharField(max_length=10)
  museum = models.CharField(max_length=50)
  museum_city = models.CharField(max_length=50)
  art_url = models.URLField(max_length=200)

  def __str__(self):
    return(f"{self.art_name} by {self.artist_name}")
