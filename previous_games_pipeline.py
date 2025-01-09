from api_files.previous_games_fetcher import get_fixture_details

def process_previous_games(fixture_ids, team_id=None):
   
    processed_games = []

    for fixture_id in fixture_ids:

        fixture_data = get_fixture_details(fixture_id)

        if fixture_data and "response" in fixture_data and fixture_data["response"]:
            fixture_info = fixture_data["response"][0]

            match_date = fixture_info["fixture"]["date"]

            home_team = fixture_info["teams"]["home"]["name"]
            away_team = fixture_info["teams"]["away"]["name"]

            goals_home = fixture_info["goals"]["home"]
            goals_away = fixture_info["goals"]["away"]

            goal_events = [
                {
                    "time_elapsed": event["time"]["elapsed"],
                    "player_name": event["player"]["name"],
                    "team_name": event["team"]["name"]
                }
                for event in fixture_info.get("events", [])
                if event["type"] == "Goal"
            ]

            team_statistics = []
            for stat in fixture_info.get("statistics", []):
                team_name = stat["team"]["name"]
                stats_data = {
                    "team_name": team_name,
                    "shots_on_goal": next(
                        (item["value"] for item in stat["statistics"] if item["type"] == "Shots on Goal"), None
                    ),
                    "shots_off_goal": next(
                        (item["value"] for item in stat["statistics"] if item["type"] == "Shots off Goal"), None
                    ),
                    "ball_possession": next(
                        (item["value"] for item in stat["statistics"] if item["type"] == "Ball Possession"), None
                    ),
                    "red_cards": next(
                        (item["value"] for item in stat["statistics"] if item["type"] == "Red Cards"), None
                    ),
                }
                team_statistics.append(stats_data)

            processed_games.append({
                "fixture_id": fixture_info["fixture"]["id"],
                "match_date": match_date,
                "home_team": home_team,
                "away_team": away_team,
                "goals": {"home": goals_home, "away": goals_away},
                "goal_events": goal_events,
                "team_statistics": team_statistics,
            })
        else:
            print(f"No data available for fixture ID {fixture_id} (Team ID: {team_id})")

    return processed_games

#testing
if __name__ == "__main__":
    specific_fixture_ids = [718701]
    previous_games = process_previous_games(specific_fixture_ids)
    for game in previous_games:
        print(game)
