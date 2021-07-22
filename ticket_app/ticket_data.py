from .hidden import ticket_api
import requests
import json

def event_search(keyword):
    endpoint = r"https://app.ticketmaster.com/discovery/v2/events"

    payload = {
        'apikey': ticket_api(),
        'keyword': keyword

    }
    content = requests.get(url = endpoint, params= payload)

    data = content.json()
    results = data['_embedded']['events']
    return results

# event_search_results = event_search('concert')
# for key, value in event_search_results.items():
#     with open('event_search_results.json', 'w') as outfile:
#         json.dump(event_search_results, outfile, indent=2)

event_search_results = event_search('concert')
for result in event_search_results:
    with open('event_search_results.json', 'w') as outfile:
        json.dump(event_search_results, outfile, indent=2)
