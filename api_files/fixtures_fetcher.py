import requests
from config import API_FOOTBALL_KEY, LEAGUE_ID, SEASON  

def get_upcoming_fixtures():
    
    url = "https://v3.football.api-sports.io/fixtures"

    
    headers = {
        'x-apisports-key': API_FOOTBALL_KEY  
    }

    
    params = {
        'league': LEAGUE_ID,
        'season': SEASON
    }

    
    response = requests.get(url, headers=headers, params=params)

    
    if response.status_code == 200:
        return response.json()  
    else:
        print("Error:", response.status_code, response.text)
        return None  

    #testing
#if __name__ == "__main__":
    specific_fixture_id = 718729  

    url = "https://v3.football.api-sports.io/fixtures"
    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }
    params = {
        'id': specific_fixture_id  
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print(response.json())  
    else:
        print("Error:", response.status_code, response.text)
