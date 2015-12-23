from django.db                          import models
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Family(models.Model):
    is_active  = models.BooleanField(default=True)
    name       = models.CharField(max_length=30)
    created_by = models.ForeignKey('UserProfile')

class UserProfile(models.Model):
    is_active       = models.BooleanField(default=True)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    profile_picture = models.ImageField()
    fam             = models.ForeignKey('Family')

class Event(models.Model):
    is_active = models.BooleanField(default=True)
    name      = models.CharField(max_length=30)
    comments  = GenericRelation('Comment')

class EventImage(models.Model):
    is_active = models.BooleanField(default=True)
    image     = models.ImageField()
    event     = models.ForeignKey('Event')
    comments  = GenericRelation('Comment')

class Comment(models.Model):
    is_active = models.BooleanField(default=True)
    author    = models.ForeignKey('UserProfile')
    comment   = models.TextField()

class FeedItem(models.Model):
    # EVERYTHING CAN BE A FEED ITEM O_O
    content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id      = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    pub_date = models.DateTimeField()

    class Meta:
        ordering = ['-pub_date']

class Opinion(models.Model):
    opinion = models.IntegerField()

    # AND YOU CAN HAVE AN OPINION ABOUT ANYTHING! O__O
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
