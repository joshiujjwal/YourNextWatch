# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Links(models.Model):
    movieid = models.TextField(db_column='movieId', blank=True, null=True)  # Field name made lowercase.
    imdbid = models.TextField(db_column='imdbId', blank=True, null=True)  # Field name made lowercase.
    tmdbid = models.TextField(db_column='tmdbId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'links'


class Movies(models.Model):
    movieid = models.IntegerField(db_column='movieId', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class Ratings(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieId', blank=True, null=True)  # Field name made lowercase.
    rating = models.TextField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'


class Tags(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieId', blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(blank=True, null=True)
    timestamp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'
