from api_files.injury_fetcher import get_injuries

def process_injuries_data(injuries_data):
    
    processed_injuries = []

    if injuries_data and "response" in injuries_data:
        for entry in injuries_data["response"]:

            player_info = {
                "player_name": entry["player"]["name"],
                "player_photo": entry["player"]["photo"],
                "injury_type": entry["player"]["type"],
                "injury_reason": entry["player"]["reason"],
                "team_name": entry["team"]["name"],
                "team_logo": entry["team"]["logo"],
                "fixture_date": entry["fixture"]["date"],
                "league_name": entry["league"]["name"],
                "league_logo": entry["league"]["logo"]
            }

            processed_injuries.append(player_info)
    
    return processed_injuries

def fetch_and_process_injuries(fixture_id):

    injuries_data = get_injuries(fixture_id=fixture_id)

    processed_data = process_injuries_data(injuries_data)

    return processed_data

#testing
#if __name__ == "__main__":
#    processed_injuries = fetch_and_process_injuries(fixture_id=718448)
    
#    if processed_injuries:
#        for injury in processed_injuries:
#            print(injury)
#    else:
#        print("No injury data available for this fixture.")

