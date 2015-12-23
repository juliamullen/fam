from django.conf.urls import url
from user.views import feed, event_view, profile_view, create_event

urlpatterns = [
        url(r'^$', feed, name="feed"),
        url(r'^profile/(?P<profile_id>\d+)/$', profile_view, name="profile"),
        url(r'^event/(?P<event_id>\d+)/$', event_view, name="event"),
        url(r'^create_event/$',                create_event, name="create-event"),
]
