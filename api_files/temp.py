import requests
from config import API_FOOTBALL_KEY

url = "https://v3.football.api-sports.io/fixtures/statistics"
headers = {'x-apisports-key': API_FOOTBALL_KEY}
params = {'fixture': 215662, 'team': 463}

response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
