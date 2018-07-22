from django.conf import settings
import requests


class GooglePlaces(object):
    BASE_API_URL = 'https://maps.googleapis.com/maps/api/place/{}/json?'

    def __init__(self):
        pass

    def get(self, endpoint, params):
        if 'key' not in params:
            params['key'] = settings.GOOGLE_PLACES_API_KEY
        url = self.BASE_API_URL.format(endpoint)
        response = requests.get(url, params=params)
        return response.json()

    def find_places(self, query):
        fields = ['formatted_address', 'icon', 'place_id', 'photos']
        params = {
            'keyword': query,
            'inputtype': 'textquery',
            'location': '19.1667478,-96.1108197',
            'radius': 1500,
            'fields': ','.join(fields)}
        results = self.get('nearbysearch', params)
        return results
