from django.contrib import admin
from user.models import Family, UserProfile, Event, EventImage, Comment, Feed

admin.site.register(Family)
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(EventImage)
admin.site.register(Comment)
admin.site.register(Feed)
