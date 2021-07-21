from requests.api import get
from ticketmaster.settings import TM_API_KEY, MAPS_API_KEY
from django.shortcuts import redirect, render
import requests
from django.conf import settings
from django.http import HttpResponse
from datetime import date
from pprint import pprint

TM_ROOT_URL = 'https://app.ticketmaster.com/discovery/v2/'
MAPS_ROOT_URL = 'https://www.google.com/maps/embed/v1/place?'
NEWS_ROOT_URL = 'https://newsapi.org/v2/'

# Helper methods


def get_artist_name_modified(artist_name, str_to_join_with):
    artist_name_slices = artist_name.split()
    artist_name_modified = str_to_join_with.join(artist_name_slices)
    return artist_name_modified


# Function views
def home(request):
    if request.method == 'POST':
        artist_name = str((request.POST)['artist_name'])
        artist_name_modified = get_artist_name_modified(artist_name, '%20')

        attraction_search_response = requests.get(
            f'{TM_ROOT_URL}attractions?apikey={settings.TM_API_KEY}&keyword={artist_name_modified}&locale=*').json()

        artists_arr = attraction_search_response['_embedded']['attractions']

        context = {'artists': artists_arr}
        return render(request, 'concerts/home.html', context)
    else:
        return render(request, 'concerts/home.html')


def show_concerts_and_news(request, artist_id):
    # Displaying concert locations
    request_url = f'{TM_ROOT_URL}events?apikey={settings.TM_API_KEY}&attractionId={artist_id}&sort=date,asc&locale=*'
    concert_search_response = requests.get(request_url).json()

    address_urls = []
    try:
        events = concert_search_response['_embedded']['events']

        for event in events:
            status = event['dates']['status']['code']
            if status == 'cancelled':
                continue
            address = event['_embedded']['venues'][0]['address']['line1']
            zipcode = event['_embedded']['venues'][0]['postalCode']
            name = event['_embedded']['venues'][0]['name']
            address_slices = address.split()
            address = '+'.join(address_slices)
            if len(address_urls) > 4:
                break
            address_urls.append(
                f'{MAPS_ROOT_URL}key={settings.MAPS_API_KEY}&q={name}+{address}+{zipcode}')
    except KeyError as e:
        print(e)

    # Getting artist_name
    artist_search_response = requests.get(
        f'{TM_ROOT_URL}attractions?apikey={settings.TM_API_KEY}&id={artist_id}&locale=*').json()
    artist_name = artist_search_response['_embedded']['attractions'][0]['name']

    # Getting news articles
    artist_name_modified = get_artist_name_modified(artist_name, '+')
    artist_name_modified = '+' + f'{artist_name_modified}'
    today = date.today()
    date_today = today.strftime("%Y-%m-%d")

    news_request_url = f'{NEWS_ROOT_URL}everything?qInTitle={artist_name_modified}&sortBy=popularity&pageSize=10&language=en&apiKey={settings.NEWS_API_KEY}'
    print(news_request_url)
    news_response = requests.get(news_request_url).json()
    articles = news_response['articles']

    context = {'artist_name': artist_name,
               'addresses': address_urls, 'articles': articles}

    return render(request, 'concerts/concerts_list.html', context)


def show_news(request, keywords):
    # if request.method == 'POST':
    #     print(request.POST)

    #     # keywords = (request.POST)['news-search']
    #     # return HttpResponse(keywords)
    #     return None
    pass
