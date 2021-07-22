from .ticket_data import event_search
from django.shortcuts import render, redirect
import requests


# Create your views here.
# take in a request, and keyword so that you can use the keyword in api request
def search_events(request):
  if request.method == 'POST':
    searched = request.POST['searched']
    results = event_search(searched)
    return render(request, 'events/search_events.html', {'searched': searched, 'results': results})
  else:
    return render(request, 'events/search_events.html', {})
