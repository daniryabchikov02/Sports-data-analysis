from datetime import datetime, timezone
from fixtures_pipeline import process_fixtures_data 

from team_stats_pipeline import fetch_team_stats  
from team_stats_formatter import format_for_chatgpt as format_team_stats 

from prediction_pipeline import process_prediction_data  
from api_files.prediction_fetcher import get_predictions  
from prediction_formatter import format_for_chatgpt as format_prediction  

from injury_pipeline import process_injuries_data 
from api_files.injury_fetcher import get_injuries 
from injury_formatter import format_injuries_for_chatgpt 

from top_scorers_pipeline import fetch_and_process_top_scorers 
from top_scorers_formatter import format_top_scorers_data 

from match_statistics_pipeline import fetch_and_process_match_statistics 
from match_statistics_formatter import format_match_statistics_data 

from api_files.past_fixtures_fetcher import get_past_fixtures 

from previous_games_pipeline import process_previous_games

manual_date = datetime(2021, 10, 10, tzinfo=timezone.utc)  


filtered_fixtures = process_fixtures_data(None, manual_date=manual_date)

DEBUG_MODE = False
if DEBUG_MODE:
    print(f"Upcoming Fixtures within the next 2 weeks ({len(filtered_fixtures)} games found):")
    for fixture in filtered_fixtures:
        print(fixture)

if filtered_fixtures:
    first_fixture = filtered_fixtures[0]
    season = first_fixture["season"] 
    team_1_id = first_fixture["home_team_id"]
    team_2_id = first_fixture["away_team_id"]
    league_id = first_fixture["league_id"]
    fixture_id = first_fixture["fixture_id"] 

    team_stats_data = fetch_team_stats(season, team_1_id, team_2_id, league_id)
    formatted_team_stats = format_team_stats(team_stats_data)
    print("Team Stats Prompt:\n", formatted_team_stats)
    
    prediction_data = get_predictions(fixture_id=fixture_id)
    processed_prediction_data = process_prediction_data(prediction_data)
    formatted_prediction = format_prediction(processed_prediction_data)
    print("\nPrediction Data Prompt:\n", formatted_prediction)

    injury_data = get_injuries(fixture_id=fixture_id)
    processed_injury_data = process_injuries_data(injury_data)
    formatted_injury_data = format_injuries_for_chatgpt(processed_injury_data)
    print("\nInjury Data Prompt:\n", formatted_injury_data)

    top_scorers_data = fetch_and_process_top_scorers(season=season, league_id=league_id, team_ids=[team_1_id, team_2_id])
    formatted_top_scorers_data = format_top_scorers_data(top_scorers_data)
    print("\nTop Scorers Data Prompt:\n", formatted_top_scorers_data)

past_fixtures_team_1 = get_past_fixtures(team_id=team_1_id, limit=5) 
past_fixtures_team_2 = get_past_fixtures(team_id=team_2_id, limit=5)

formatted_match_statistics_team_1 = process_previous_games(past_fixtures_team_1, team_id=team_1_id)
print("\nMatch Statistics Data for Team 1:\n", formatted_match_statistics_team_1)

formatted_match_statistics_team_2 = process_previous_games(past_fixtures_team_2, team_id=team_2_id)
print("\nMatch Statistics Data for Team 2:\n", formatted_match_statistics_team_2)








# Future integration:
# For additional data, import and handle similar pipelines here, e.g., injuries_pipeline
# from injuries_pipeline import data as injuries_data
# Format and print injury stats once they are integrated


#improve the stat selection