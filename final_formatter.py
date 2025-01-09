def optimize_output(data):
    
    output = []

    team_stats = data.get("team_stats", {})
    if team_stats:
        output.append("**Team Analysis**")
        output.append(team_stats)

    prediction_data = data.get("prediction_data", {})
    if prediction_data:
        output.append("\n**Prediction Summary**")
        prediction_summary = "Predicted Winner: {winner}\nWin/Draw: {win_draw}\nGoal Advice: {goal_advice}\n".format(
            winner=prediction_data.get("Predicted Winner", "Unknown"),
            win_draw=prediction_data.get("Win or Draw", "Unknown"),
            goal_advice=prediction_data.get("Goal Advice", "None"),
        )
        output.append(prediction_summary)

    injury_data = data.get("injury_data", "No injury data available.")
    output.append("\n**Injury Report**")
    output.append(injury_data if injury_data != "No injury data available." else "No injuries reported.")

    top_scorers_data = data.get("top_scorers_data", [])
    if top_scorers_data:
        output.append("\n**Top Scorers Summary**")
        for player in top_scorers_data[:3]:
            output.append("- {name} ({team}): {goals} goals, {assists} assists".format(
                name=player.get("Player", "Unknown"),
                team=player.get("Team Name", "Unknown"),
                goals=player.get("Goals Scored", 0),
                assists=player.get("Assists", 0),
            ))

    match_statistics = data.get("match_statistics", {})
    team_1_stats = match_statistics.get("team_1", [])
    team_2_stats = match_statistics.get("team_2", [])

    if team_1_stats or team_2_stats:
        output.append("\n**Recent Match Statistics**")
        if team_1_stats:
            output.append("Team 1 Summary:")
            output.append(summarize_match_statistics(team_1_stats))
        if team_2_stats:
            output.append("Team 2 Summary:")
            output.append(summarize_match_statistics(team_2_stats))

    return "\n".join(output)

def summarize_match_statistics(match_stats):
    
    summary = []
    for match in match_stats[:3]:
        summary.append("- {home_team} {home_goals}-{away_goals} {away_team} ({date})".format(
            home_team=match.get("home_team", "Unknown"),
            home_goals=match.get("goals", {}).get("home", 0),
            away_goals=match.get("goals", {}).get("away", 0),
            away_team=match.get("away_team", "Unknown"),
            date=match.get("match_date", "Unknown"),
        ))
    return "\n".join(summary)

#testing
#if __name__ == "__main__":
    sample_data = {
        "team_stats": "Team stats for Paris Saint Germain vs Angers",
        "prediction_data": {
            "Predicted Winner": "Paris Saint Germain",
            "Win or Draw": "Yes",
            "Goal Advice": "Double chance: PSG or draw",
        },
        "injury_data": "No injuries reported",
        "top_scorers_data": [
            {"Player": "Kylian Mbappé", "Team Name": "Paris Saint Germain", "Goals Scored": 28, "Assists": 17},
            {"Player": "Neymar", "Team Name": "Paris Saint Germain", "Goals Scored": 13, "Assists": 6},
        ],
        "match_statistics": {
            "team_1": [
                {"home_team": "PSG", "away_team": "Metz", "goals": {"home": 5, "away": 0}, "match_date": "2022-05-21"},
                {"home_team": "PSG", "away_team": "Troyes", "goals": {"home": 2, "away": 2}, "match_date": "2022-05-08"},
            ],
            "team_2": [
                {"home_team": "Angers", "away_team": "Montpellier", "goals": {"home": 2, "away": 0}, "match_date": "2022-05-21"},
            ],
        },
    }

    print(optimize_output(sample_data))
