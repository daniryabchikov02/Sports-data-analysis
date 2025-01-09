import requests
from config import API_FOOTBALL_KEY

def get_predictions(fixture_id):
    
    url = "https://v3.football.api-sports.io/predictions"

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
if __name__ == "__main__":
    fixture_id = 198772
    predictions = get_predictions(fixture_id)
    print("Predictions:", predictions)
