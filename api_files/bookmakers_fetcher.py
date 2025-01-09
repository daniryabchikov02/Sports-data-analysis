import requests
from config import API_FOOTBALL_KEY 

def fetch_bookmakers():
    
    url = "https://v3.football.api-sports.io/odds/bookmakers"

    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }

    try:
        response = requests.get(url, headers=headers)

       
        if response.status_code == 200:
            return response.json()  
        else:
            print(f"Error fetching bookmakers: {response.status_code} - {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"RequestException while fetching bookmakers: {e}")
        return None

#testing
if __name__ == "__main__":
    bookmakers_data = fetch_bookmakers()
    if bookmakers_data:
        print(bookmakers_data)
