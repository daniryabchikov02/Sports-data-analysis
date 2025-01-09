import requests
from config import API_FOOTBALL_KEY

def get_recent_player_performance(player_ids, fixture_ids):
    url = "https://v3.football.api-sports.io/players"

    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }

    params = {
        'players': ','.join(map(str, player_ids)),  
        'fixtures': ','.join(map(str, fixture_ids))  
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Response Data:", data) 
        return data
    else:
        print("Error:", response.status_code, response.text)
        return None

#testing
if __name__ == "__main__":
    test_player_ids = [123, 456]
    test_fixture_ids = [789, 1011]
    get_recent_player_performance(test_player_ids, test_fixture_ids)
