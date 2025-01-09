from api_files.prediction_fetcher import get_predictions
from prediction_formatter import format_for_chatgpt

def process_prediction_data(prediction_data):

    processed_data = {
        "winner_prediction": None,
        "win_or_draw": None,
        "goal_advice": None,
        "goal_under_over": None,
        "percentages": {},
        "home_team_last_5": {},
        "away_team_last_5": {},
        "comparison": {},
        "h2h": []
    }
    
    if prediction_data and "response" in prediction_data:
        response = prediction_data["response"][0]
        
        predictions = response.get("predictions", {})
        processed_data["winner_prediction"] = predictions.get("winner", {}).get("name")
        processed_data["win_or_draw"] = predictions.get("win_or_draw")
        processed_data["goal_advice"] = predictions.get("advice")
        processed_data["goal_under_over"] = predictions.get("under_over")
        processed_data["percentages"] = predictions.get("percent", {})

        home_team = response.get("teams", {}).get("home", {})
        processed_data["home_team_last_5"] = home_team.get("last_5", {})
        
        away_team = response.get("teams", {}).get("away", {})
        processed_data["away_team_last_5"] = away_team.get("last_5", {})
        
        processed_data["comparison"] = {
            "form": response.get("comparison", {}).get("form", {}),
            "att": response.get("comparison", {}).get("att", {}),
            "def": response.get("comparison", {}).get("def", {}),
            "poisson_distribution": response.get("comparison", {}).get("poisson_distribution", {}),
            "h2h": response.get("comparison", {}).get("h2h", {}),
            "goals": response.get("comparison", {}).get("goals", {}),
            "total": response.get("comparison", {}).get("total", {})
        }

        h2h_data = response.get("h2h", [])
        for match in h2h_data:
            h2h_match = {
                "fixture_id": match["fixture"].get("id"),
                "date": match["fixture"].get("date"),
                "venue": match["fixture"].get("venue", {}).get("name"),
                "home_team": match["teams"]["home"]["name"],
                "away_team": match["teams"]["away"]["name"],
                "league": {
                    "name": match["league"]["name"],
                    "country": match["league"]["country"],
                    "season": match["league"]["season"],
                    "round": match["league"].get("round")
                },
                "goals": {
                    "home": match["goals"].get("home"),
                    "away": match["goals"].get("away")
                },
                "score": {
                    "halftime": match["score"].get("halftime"),
                    "fulltime": match["score"].get("fulltime"),
                    "extratime": match["score"].get("extratime"),
                    "penalty": match["score"].get("penalty")
                },
                "home_winner": match["teams"]["home"].get("winner"),
                "away_winner": match["teams"]["away"].get("winner")
            }
            processed_data["h2h"].append(h2h_match)
    
    return processed_data

def fetch_and_format_prediction(fixture_id):

    prediction_data = get_predictions(fixture_id=fixture_id)
    
    processed_data = process_prediction_data(prediction_data)
    
    formatted_data = format_for_chatgpt(processed_data)
    
    return formatted_data
