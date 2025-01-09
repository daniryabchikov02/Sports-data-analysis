import requests
from config import API_FOOTBALL_KEY
import time

def get_fixture_details(fixture_id):
    
    url = "https://v3.football.api-sports.io/fixtures"

    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }

    params = {
        'id': fixture_id 
    }
    
    time.sleep(0.5)

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

#testing
#if __name__ == "__main__":
    specific_fixture_ids = [718729]

    for fixture_id in specific_fixture_ids:
        fixture_details = get_fixture_details(fixture_id)
        print(f"Fixture ID {fixture_id} Details:", fixture_details)
