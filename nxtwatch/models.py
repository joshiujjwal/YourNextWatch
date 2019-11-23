import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Links(models.Model):
    movieid = models.TextField(primary_key=True)  # Field name made lowercase.
    imdbid = models.TextField(blank=True, null=True)  # Field name made lowercase.
    tmdbid = models.TextField(blank=True, null=True)  # Field name made lowercase.



class Movies(models.Model):
    movieid = models.IntegerField(primary_key=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)




class Ratings(models.Model):
    userid = models.TextField(blank=True, null=True)  # Field name made lowercase.
    movieid = models.IntegerField(blank=False, null=False)
    rating = models.FloatField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
    



class Tags(models.Model):
    userid = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    movieid = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)
