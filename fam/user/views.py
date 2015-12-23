from django.shortcuts import render_to_response
from user.models import FeedItem
from user.forms  import EventForm

def feed(request):
    feed_items = FeedItem.objects.all()

    context = {
        'feed': feed_items,
    }

    return render_to_response('user/feed.html', context)

def event_view(request):
    pass

def profile_view(request):
    pass

def create_event(request):
    event_form = EventForm()

    context = {
        'form': event_form,
    }

    return render_to_response('user/create_event.html', context)
