from api_files.top_scorers_fetcher import get_top_scorers

def process_top_scorers_data(top_scorers_data, team_ids):

    processed_scorers = []

    if top_scorers_data and "response" in top_scorers_data:
        for entry in top_scorers_data["response"]:
            if entry["statistics"][0]["team"]["id"] in team_ids:
                scorer_info = {
                    "player_name": entry["player"]["name"],
                    "age": entry["player"]["age"],
                    "nationality": entry["player"]["nationality"],
                    "team_name": entry["statistics"][0]["team"]["name"],
                    "games_appearances": entry["statistics"][0]["games"]["appearences"],
                    "games_lineups": entry["statistics"][0]["games"]["lineups"],
                    "games_minutes": entry["statistics"][0]["games"]["minutes"],
                    "games_position": entry["statistics"][0]["games"]["position"],
                    "games_rating": entry["statistics"][0]["games"]["rating"],
                    "games_captain": entry["statistics"][0]["games"]["captain"],
                    "substitutes_in": entry["statistics"][0]["substitutes"]["in"],
                    "substitutes_out": entry["statistics"][0]["substitutes"]["out"],
                    "substitutes_bench": entry["statistics"][0]["substitutes"]["bench"],
                    "shots_total": entry["statistics"][0]["shots"]["total"],
                    "shots_on": entry["statistics"][0]["shots"]["on"],
                    "goals_total": entry["statistics"][0]["goals"]["total"],
                    "goals_conceded": entry["statistics"][0]["goals"]["conceded"],
                    "goals_assists": entry["statistics"][0]["goals"]["assists"],
                    "passes_total": entry["statistics"][0]["passes"]["total"],
                    "passes_key": entry["statistics"][0]["passes"]["key"],
                    "passes_accuracy": entry["statistics"][0]["passes"]["accuracy"],
                    "tackles_total": entry["statistics"][0]["tackles"]["total"],
                    "duels_total": entry["statistics"][0]["duels"]["total"],
                    "duels_won": entry["statistics"][0]["duels"]["won"],
                    "dribbles_attempts": entry["statistics"][0]["dribbles"]["attempts"],
                    "dribbles_success": entry["statistics"][0]["dribbles"]["success"],
                    "fouls_drawn": entry["statistics"][0]["fouls"]["drawn"],
                    "fouls_committed": entry["statistics"][0]["fouls"]["committed"],
                    "cards_yellow": entry["statistics"][0]["cards"]["yellow"],
                    "cards_yellowred": entry["statistics"][0]["cards"]["yellowred"],
                    "cards_red": entry["statistics"][0]["cards"]["red"],
                    "penalty_won": entry["statistics"][0]["penalty"]["won"],
                    "penalty_scored": entry["statistics"][0]["penalty"]["scored"],
                    "penalty_missed": entry["statistics"][0]["penalty"]["missed"]
                }
                processed_scorers.append(scorer_info)

    return processed_scorers

def fetch_and_process_top_scorers(season, league_id, team_ids):
    top_scorers_data = get_top_scorers(season=season, league_id=league_id)

    processed_data = process_top_scorers_data(top_scorers_data, team_ids)

    return processed_data

#testing
#if __name__ == "__main__":
#    team_ids = [85, 91]
#    processed_scorers = fetch_and_process_top_scorers(season=2021, league_id=61, team_ids=team_ids)
#    for scorer in processed_scorers:
#        print(scorer)
