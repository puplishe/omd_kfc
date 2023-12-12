import requests


def get_api_data(url='https://api.prod.digital.uni.rest/api/store/v2/store.get_restaurants?showClosed=false'):
    response = requests.get(url)
    response = response.json()
    response = response['searchResults']
    return response
