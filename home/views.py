from django.shortcuts import render
import requests
from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def home(request):
    # Your Steam API logic here
    api_key = 'API KEY'
    steam_id = 'steamID'

    api_url = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        data = {'response': {'player_level': 'N/A'}}

    return render(request, 'home/index.html', {'steam_data': data})
