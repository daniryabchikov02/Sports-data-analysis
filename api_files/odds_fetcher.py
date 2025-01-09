import requests
from config import API_FOOTBALL_KEY


def get_odds(season=2021, bet_type=1, bookmaker_id=6, fixture_id=157140, league_id=39):
    
    url = "https://v3.football.api-sports.io/odds"

    
    headers = {
        'x-apisports-key': API_FOOTBALL_KEY
    }

    
    params = {
        'season': season,
        'bet': bet_type,        
        'bookmaker': bookmaker_id,  
        'fixture': fixture_id,   
        'league': league_id      
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()  
        odds_data = data.get("response", [])

        structured_odds = []
        for item in odds_data:
            for bookmaker in item.get("bookmakers", []):
                odds_details = {
                    "fixture_id": fixture_id,
                    "league": league_id,
                    "home_team_odds": bookmaker.get("bets", [])[0].get("values", [])[0].get("odd", "N/A"),
                    "draw_odds": bookmaker.get("bets", [])[0].get("values", [])[1].get("odd", "N/A"),
                    "away_team_odds": bookmaker.get("bets", [])[0].get("values", [])[2].get("odd", "N/A"),
                    "bookmaker_name": bookmaker.get("name", "N/A")
                }
                structured_odds.append(odds_details)
        
        print(f"Retrieved odds for fixture {fixture_id} with bookmaker ID {bookmaker_id}.")
        return structured_odds
    else:
        print("Error:", response.status_code, response.text)
        return None

#testing
if __name__ == "__main__":
    odds = get_odds()
    for odd in odds:
        print(f"Fixture ID: {odd['fixture_id']}, League: {odd['league']}")
        print(f"  Home Team Odds: {odd['home_team_odds']}")
        print(f"  Draw Odds: {odd['draw_odds']}")
        print(f"  Away Team Odds: {odd['away_team_odds']}")
        print(f"  Bookmaker: {odd['bookmaker_name']}\n")
