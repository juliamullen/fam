from django.shortcuts import render_to_response
from user.models import Feed

def feed(request):
    feed_items = Feed.objects.all()
    return render_to_response('user/feed.html', context)

def event_view(request):
    pass

def profile_view(request):
    pass
