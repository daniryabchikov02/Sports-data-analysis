import requests
from config import API_FOOTBALL_KEY

def get_team_stats(season=2021, team_id=541, league_id=140):

    url = "https://v3.football.api-sports.io/teams/statistics"

    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }

    params = {
        'season': season,
        'team': team_id,  
        'league': league_id  
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
    stats = get_team_stats()
    print("Team Stats:", stats)
