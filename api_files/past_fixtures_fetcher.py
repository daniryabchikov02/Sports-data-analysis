import requests
from config import API_FOOTBALL_KEY, SEASON
from datetime import datetime

def get_past_fixtures(team_id, limit=5):
    
    url = "https://v3.football.api-sports.io/fixtures"

    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }

    params = {
        'team': team_id,
        'season': SEASON, 
        #'status': 'FT'  
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        fixtures_data = response.json()
        fixtures = fixtures_data.get("response", [])

        fixtures.sort(key=lambda x: datetime.fromisoformat(x["fixture"]["date"].replace("Z", "+00:00")), reverse=True)

        fixture_ids = [fixture["fixture"]["id"] for fixture in fixtures[:limit]]
        return fixture_ids
    else:
        print("Error:", response.status_code, response.text)
        return []

#testing
#if __name__ == "__main__":
    team_id = 85  # Example team ID
    past_fixtures = get_past_fixtures(team_id)
    print("Past Fixture IDs:", past_fixtures)
