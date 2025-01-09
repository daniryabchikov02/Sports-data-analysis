from api_files.team_stats_fetcher import get_team_stats 
from team_stats_formatter import format_for_chatgpt

def fetch_team_stats(season, team_1_id, team_2_id, league_id):
    
    team_1_data = get_team_stats(season=season, team_id=team_1_id, league_id=league_id)
    team_2_data = get_team_stats(season=season, team_id=team_2_id, league_id=league_id)

    data = {
        "league_info": {
            "league_id": None,
            "league_name": None,
            "country": None,
            "season": None,
            "logo": None,
            "flag": None
        },
        "team_1_info": { 
            "team_id": None,
            "team_name": None,
            "form": None,
            "logo": None,
            "fixtures": {"played": {"home": None, "away": None, "total": None}, "wins": {}, "draws": {}, "loses": {}},
            "goals": {"for": {}, "against": {}},
            "under_over": {"for": {}, "against": {}},
            "biggest": {"streak": {}, "wins": {}, "loses": {}, "goals": {}},
            "clean_sheet": {},
            "failed_to_score": {},
            "penalty": {"scored": {}, "missed": {}, "total": None},
            "lineups": [],
            "cards": {"yellow": {}, "red": {}}
        },
        "team_2_info": {  
            "team_id": None,
            "team_name": None,
            "form": None,
            "logo": None,
            "fixtures": {"played": {"home": None, "away": None, "total": None}, "wins": {}, "draws": {}, "loses": {}},
            "goals": {"for": {}, "against": {}},
            "under_over": {"for": {}, "against": {}},
            "biggest": {"streak": {}, "wins": {}, "loses": {}, "goals": {}},
            "clean_sheet": {},
            "failed_to_score": {},
            "penalty": {"scored": {}, "missed": {}, "total": None},
            "lineups": [],
            "cards": {"yellow": {}, "red": {}}
        }
    }

    if team_1_data and "response" in team_1_data:
        response_1 = team_1_data["response"]
        if data["league_info"]["league_id"] is None:
            data["league_info"]["league_id"] = response_1.get("league", {}).get("id")
            data["league_info"]["league_name"] = response_1.get("league", {}).get("name")
            data["league_info"]["country"] = response_1.get("league", {}).get("country")
            data["league_info"]["season"] = response_1.get("league", {}).get("season")
            data["league_info"]["logo"] = response_1.get("league", {}).get("logo")
            data["league_info"]["flag"] = response_1.get("league", {}).get("flag")
        data["team_1_info"]["team_id"] = response_1["team"].get("id", data["team_1_info"]["team_id"])
        data["team_1_info"]["team_name"] = response_1["team"].get("name", data["team_1_info"]["team_name"])
        data["team_1_info"]["form"] = response_1.get("form", data["team_1_info"]["form"])
        data["team_1_info"]["logo"] = response_1["team"].get("logo", data["team_1_info"]["logo"])
        data["team_1_info"]["fixtures"] = response_1.get("fixtures", data["team_1_info"]["fixtures"])
        data["team_1_info"]["goals"] = response_1.get("goals", data["team_1_info"]["goals"])
        data["team_1_info"]["goals"]["for"]["minute"] = response_1["goals"]["for"].get("minute", data["team_1_info"]["goals"]["for"].get("minute", {}))
        data["team_1_info"]["goals"]["against"]["minute"] = response_1["goals"]["against"].get("minute", data["team_1_info"]["goals"]["against"].get("minute", {}))

        data["team_1_info"]["under_over"]["for"] = response_1["goals"]["for"].get("under_over", data["team_1_info"]["under_over"]["for"])
        data["team_1_info"]["under_over"]["against"] = response_1["goals"]["against"].get("under_over", data["team_1_info"]["under_over"]["against"])

        data["team_1_info"]["under_over"]["for"] = response_1["goals"]["for"].get("under_over", data["team_1_info"]["under_over"]["for"])
        data["team_1_info"]["under_over"]["against"] = response_1["goals"]["against"].get("under_over", data["team_1_info"]["under_over"]["against"])
        data["team_1_info"]["biggest"] = response_1.get("biggest", data["team_1_info"]["biggest"])

        data["team_1_info"]["biggest"]["streak"] = response_1["biggest"].get("streak", data["team_1_info"]["biggest"].get("streak", {}))
        data["team_1_info"]["biggest"]["wins"] = response_1["biggest"].get("wins", data["team_1_info"]["biggest"].get("wins", {}))
        data["team_1_info"]["biggest"]["loses"] = response_1["biggest"].get("loses", data["team_1_info"]["biggest"].get("loses", {}))
        data["team_1_info"]["biggest"]["goals"] = response_1["biggest"].get("goals", data["team_1_info"]["biggest"].get("goals", {}))

        data["team_1_info"]["clean_sheet"] = response_1.get("clean_sheet", data["team_1_info"]["clean_sheet"])
        data["team_1_info"]["failed_to_score"] = response_1.get("failed_to_score", data["team_1_info"]["failed_to_score"])
        data["team_1_info"]["penalty"] = response_1.get("penalty", data["team_1_info"]["penalty"])
        data["team_1_info"]["lineups"] = response_1.get("lineups", data["team_1_info"]["lineups"])

        data["team_1_info"]["lineups"] = response_1.get("lineups", data["team_1_info"]["lineups"])
        data["team_1_info"]["cards"]["yellow"] = response_1["cards"].get("yellow", data["team_1_info"]["cards"].get("yellow", {}))
        data["team_1_info"]["cards"]["red"] = response_1["cards"].get("red", data["team_1_info"]["cards"].get("red", {}))

        data["team_1_info"]["cards"] = response_1.get("cards", data["team_1_info"]["cards"])

    if team_2_data and "response" in team_2_data:
        response_2 = team_2_data["response"]
        data["team_2_info"]["team_id"] = response_2["team"].get("id", data["team_2_info"]["team_id"])
        data["team_2_info"]["team_name"] = response_2["team"].get("name", data["team_2_info"]["team_name"])
        data["team_2_info"]["form"] = response_2.get("form", data["team_2_info"]["form"])
        data["team_2_info"]["logo"] = response_2["team"].get("logo", data["team_2_info"]["logo"])
        data["team_2_info"]["fixtures"] = response_2.get("fixtures", data["team_2_info"]["fixtures"])
        data["team_2_info"]["goals"] = response_2.get("goals", data["team_2_info"]["goals"])
        data["team_2_info"]["goals"]["for"]["minute"] = response_2["goals"]["for"].get("minute", data["team_2_info"]["goals"]["for"].get("minute", {}))
        data["team_2_info"]["goals"]["against"]["minute"] = response_2["goals"]["against"].get("minute", data["team_2_info"]["goals"]["against"].get("minute", {}))


        data["team_2_info"]["under_over"]["for"] = response_2["goals"]["for"].get("under_over", data["team_2_info"]["under_over"]["for"])
        data["team_2_info"]["under_over"]["against"] = response_2["goals"]["against"].get("under_over", data["team_2_info"]["under_over"]["against"])
        data["team_2_info"]["under_over"]["for"] = response_2["goals"]["for"].get("under_over", data["team_2_info"]["under_over"]["for"])
        data["team_2_info"]["under_over"]["against"] = response_2["goals"]["against"].get("under_over", data["team_2_info"]["under_over"]["against"])
        data["team_2_info"]["biggest"] = response_2.get("biggest", data["team_2_info"]["biggest"])
        data["team_2_info"]["biggest"]["streak"] = response_2["biggest"].get("streak", data["team_2_info"]["biggest"].get("streak", {}))
        data["team_2_info"]["biggest"]["wins"] = response_2["biggest"].get("wins", data["team_2_info"]["biggest"].get("wins", {}))
        data["team_2_info"]["biggest"]["loses"] = response_2["biggest"].get("loses", data["team_2_info"]["biggest"].get("loses", {}))
        data["team_2_info"]["biggest"]["goals"] = response_2["biggest"].get("goals", data["team_2_info"]["biggest"].get("goals", {}))
        data["team_2_info"]["clean_sheet"] = response_2.get("clean_sheet", data["team_2_info"]["clean_sheet"])
        data["team_2_info"]["failed_to_score"] = response_2.get("failed_to_score", data["team_2_info"]["failed_to_score"])
        data["team_2_info"]["penalty"] = response_2.get("penalty", data["team_2_info"]["penalty"])
        data["team_2_info"]["lineups"] = response_2.get("lineups", data["team_2_info"]["lineups"])
        data["team_2_info"]["lineups"] = response_2.get("lineups", data["team_2_info"]["lineups"])
        data["team_2_info"]["cards"]["yellow"] = response_2["cards"].get("yellow", data["team_2_info"]["cards"].get("yellow", {}))
        data["team_2_info"]["cards"]["red"] = response_2["cards"].get("red", data["team_2_info"]["cards"].get("red", {}))
        data["team_2_info"]["cards"] = response_2.get("cards", data["team_2_info"]["cards"])

   
    return data
    
