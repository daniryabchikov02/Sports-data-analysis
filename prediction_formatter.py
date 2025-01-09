def format_for_chatgpt(prediction_data):

    formatted_output = (
        f"**Prediction Analysis**\n"
        
        f"**Winner Prediction:**\n"
        f"  - Predicted Winner: {prediction_data.get('winner_prediction', 'N/A')}\n"
        f"  - Win or Draw: {'Yes' if prediction_data.get('win_or_draw') else 'No'}\n"
        f"  - Goal Advice: {prediction_data.get('goal_advice', 'N/A')}\n"
        f"  - Under/Over Advice: {prediction_data.get('goal_under_over', 'N/A')}\n\n"

        f"**Outcome Percentages:**\n"
        f"  - Home Win: {prediction_data['percentages'].get('home', 'N/A')}\n"
        f"  - Draw: {prediction_data['percentages'].get('draw', 'N/A')}\n"
        f"  - Away Win: {prediction_data['percentages'].get('away', 'N/A')}\n\n"
        
        f"**Home Team Last 5 Games:**\n"
        f"  - Form: {prediction_data['home_team_last_5'].get('form', 'N/A')}\n"
        f"  - Attack Performance: {prediction_data['home_team_last_5'].get('att', 'N/A')}\n"
        f"  - Defense Performance: {prediction_data['home_team_last_5'].get('def', 'N/A')}\n"
        f"  - Goals For (Total): {prediction_data['home_team_last_5'].get('goals', {}).get('for', {}).get('total', 'N/A')}\n"
        f"  - Goals Against (Total): {prediction_data['home_team_last_5'].get('goals', {}).get('against', {}).get('total', 'N/A')}\n\n"

        f"**Away Team Last 5 Games:**\n"
        f"  - Form: {prediction_data['away_team_last_5'].get('form', 'N/A')}\n"
        f"  - Attack Performance: {prediction_data['away_team_last_5'].get('att', 'N/A')}\n"
        f"  - Defense Performance: {prediction_data['away_team_last_5'].get('def', 'N/A')}\n"
        f"  - Goals For (Total): {prediction_data['away_team_last_5'].get('goals', {}).get('for', {}).get('total', 'N/A')}\n"
        f"  - Goals Against (Total): {prediction_data['away_team_last_5'].get('goals', {}).get('against', {}).get('total', 'N/A')}\n\n"

        f"**Team Comparison:**\n"
        f"  - Form Comparison: Home {prediction_data['comparison'].get('form', {}).get('home', 'N/A')}, Away {prediction_data['comparison'].get('form', {}).get('away', 'N/A')}\n"
        f"  - Attack Comparison: Home {prediction_data['comparison'].get('att', {}).get('home', 'N/A')}, Away {prediction_data['comparison'].get('att', {}).get('away', 'N/A')}\n"
        f"  - Defense Comparison: Home {prediction_data['comparison'].get('def', {}).get('home', 'N/A')}, Away {prediction_data['comparison'].get('def', {}).get('away', 'N/A')}\n"
        f"  - Poisson Distribution: Home {prediction_data['comparison'].get('poisson_distribution', {}).get('home', 'N/A')}, Away {prediction_data['comparison'].get('poisson_distribution', {}).get('away', 'N/A')}\n"
        f"  - H2H Win Ratio: Home {prediction_data['comparison'].get('h2h', {}).get('home', 'N/A')}, Away {prediction_data['comparison'].get('h2h', {}).get('away', 'N/A')}\n"
        f"  - Goals Comparison: Home {prediction_data['comparison'].get('goals', {}).get('home', 'N/A')}, Away {prediction_data['comparison'].get('goals', {}).get('away', 'N/A')}\n"
        f"  - Total Comparison: Home {prediction_data['comparison'].get('total', {}).get('home', 'N/A')}, Away {prediction_data['comparison'].get('total', {}).get('away', 'N/A')}\n\n"
        
        f"**Head-to-Head (H2H) Matches:**\n"
    )

    for match in prediction_data.get("h2h", []):
        formatted_output += (
            f"  - Date: {match.get('date', 'N/A')}\n"
            f"    Venue: {match.get('venue', 'N/A')}\n"
            f"    League: {match.get('league', {}).get('name', 'N/A')} ({match.get('league', {}).get('country', 'N/A')})\n"
            f"    {match.get('home_team', 'N/A')} vs {match.get('away_team', 'N/A')}\n"
            f"    Score: {match.get('goals', {}).get('home', 'N/A')} - {match.get('goals', {}).get('away', 'N/A')} (Fulltime)\n"
            f"    Halftime Score: {match.get('score', {}).get('halftime', {}).get('home', 'N/A')} - {match.get('score', {}).get('halftime', {}).get('away', 'N/A')}\n"
            f"    Extra Time Score: {match.get('score', {}).get('extratime', {}).get('home', 'N/A')} - {match.get('score', {}).get('extratime', {}).get('away', 'N/A')}\n"
            f"    Penalty Score: {match.get('score', {}).get('penalty', {}).get('home', 'N/A')} - {match.get('score', {}).get('penalty', {}).get('away', 'N/A')}\n"
            f"    Result: Home Win: {'Yes' if match.get('home_winner') else 'No'}, Away Win: {'Yes' if match.get('away_winner') else 'No'}\n\n"
        )
    
    return formatted_output
