from django.conf.urls import url
from user.views import feed, event_view, profile_view

urlpatterns = [
        url(r'^$', feed, name="feed"),
        url(r'^profile/(?P<profile_id>\d+)/$', profile_view, name="profile"),
        url(r'^event/(?P<event_id>\d+/$', event_view, name="event"),
]
