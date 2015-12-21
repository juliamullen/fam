from django.shortcuts import render
from user.models import

def feed(request):
    return render(request, 'user/feed.html', {})

def event_view(request):
    pass

def profile_view(request):
    pass
