import requests
from config import API_FOOTBALL_KEY


def get_match_statistics(fixture_id, team_id):

    url = "https://v3.football.api-sports.io/fixtures/statistics"

    
    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }

    
    params = {
        'fixture': fixture_id,
        'team': team_id
    }

    
    response = requests.get(url, headers=headers, params=params)

    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code, response.text)
        return None

#testing
if __name__ == "__main__":
    match_stats = get_match_statistics(fixture_id=718721, team_id=77)
    print("Match Statistics Data:", match_stats)
