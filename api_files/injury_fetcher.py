import requests
from config import API_FOOTBALL_KEY


def get_injuries(fixture_id):
    
    url = "https://v3.football.api-sports.io/injuries"

    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }

    params = {
        'fixture': fixture_id
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code, response.text)
        return None

#testing
#if __name__ == "__main__":
#    injuries = get_injuries(fixture_id=686314)
#    print("Injuries Data:", injuries)
