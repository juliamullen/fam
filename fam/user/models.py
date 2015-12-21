from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

class Family(models.Model):
    name = models.CharField(max_length=30)

class UserProfile(models.Model):
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    profile_picture = models.ImageField()
    family          = models.ForeignKey('Family')

class Event(models.Model):
    name = models.CharField(max_length=30)
    comments = GenericRelation('Comment')

class EventImage(models.Model):
    image = models.ImageField()
    event = models.ForeignKey('Event')
    comments = GenericRelation('Comment')

class Comment(models.Model):
    author  = models.ForeignKey('UserProfile')
    comment = models.TextField()

class Feed(models.Model):
    EVENT_CHOICES = (
        ('l', 'Like'),
        ('p', 'Post'),
        ('c', 'Comment'),
    )
    feed_event = models.CharField(max_length=1, choices=EVENT_CHOICES)
    user       = models.ForeignKey('UserProfile')
