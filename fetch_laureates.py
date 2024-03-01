import os
import django

# Configure the environment for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nobel_laureates_endpoints.settings')
django.setup()

from nobels.models import Laureate
import requests


def fetch_and_store_laureates():
    response = requests.get('http://api.nobelprize.org/v1/prize.json?category=economics')
    prizes = response.json().get('prizes', [])

    for prize in prizes:
        year = prize['year']
        for laureate in prize['laureates']:
            name = laureate.get('firstname', '') + ' ' + laureate.get('surname', '')
            contribution = laureate.get('motivation', '').strip('"')
            Laureate.objects.get_or_create(name=name, year=year, contribution=contribution)


if __name__ == "__main__":
    fetch_and_store_laureates()
