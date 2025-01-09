import requests
from config import API_FOOTBALL_KEY

def get_top_scorers(season, league_id):
    
    url = "https://v3.football.api-sports.io/players/topscorers"

    
    headers = {
        'x-apisports-key': API_FOOTBALL_KEY  
    }

    params = {
        'season': season,
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
    top_scorers = get_top_scorers(season=2021, league_id=61)
    print("Top Scorers Data:", top_scorers)
