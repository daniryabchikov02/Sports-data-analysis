from api_files.match_statistics_fetcher import get_match_statistics

def process_match_statistics_data(statistics_data):
    
    processed_statistics = {}

    if statistics_data and "response" in statistics_data and statistics_data["response"]:
        team_data = statistics_data["response"][0]
        
        processed_statistics = {
            "team_name": team_data["team"]["name"],
            "team_logo": team_data["team"]["logo"]
        }

        for stat in team_data["statistics"]:
            processed_statistics[stat["type"]] = stat["value"]
    
    return processed_statistics

def fetch_and_process_match_statistics(fixture_ids, team_ids):
    
    all_statistics = []

    for fixture_id in fixture_ids:
        for team_id in team_ids:

            statistics_data = get_match_statistics(fixture_id=fixture_id, team_id=team_id)

            if statistics_data and "response" in statistics_data and statistics_data["response"]:

                processed_data = process_match_statistics_data(statistics_data)
                all_statistics.append({
                    "fixture_id": fixture_id,
                    "team_id": team_id,
                    "statistics": processed_data
                })
            else:
                all_statistics.append({
                    "fixture_id": fixture_id,
                    "team_id": team_id,
                    "statistics": None 
                })

    return all_statistics


#testing
if __name__ == "__main__":
    fixture_ids = [215662, 215663, 215664, 215665, 215666] 
    team_ids = [463, 464]
    statistics_data = fetch_and_process_match_statistics(fixture_ids, team_ids)
    for stats in statistics_data:
        print(stats)