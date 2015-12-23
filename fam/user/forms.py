from django.forms import ModelForm
from user.models  import Event

class EventForm(ModelForm):
    class Meta:
        model  = Event
        fields = ['name']
