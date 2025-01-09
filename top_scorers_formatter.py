def format_top_scorers_data(top_scorers_data):
    formatted_output = "**Top Scorers Data**\n"

    for scorer in top_scorers_data:
        formatted_output += (
            f"\n**Player:** {scorer.get('player_name', 'N/A')}\n"
            f"  - Age: {scorer.get('age', 'N/A')}\n"
            f"  - Nationality: {scorer.get('nationality', 'N/A')}\n"
            f"  - Team Name: {scorer.get('team_name', 'N/A')}\n\n"

            f"**Game Stats:**\n"
            f"  - Appearances: {scorer.get('games_appearances', 'N/A')}\n"
            f"  - Lineups: {scorer.get('games_lineups', 'N/A')}\n"
            f"  - Minutes: {scorer.get('games_minutes', 'N/A')}\n"
            f"  - Position: {scorer.get('games_position', 'N/A')}\n"
            f"  - Rating: {scorer.get('games_rating', 'N/A')}\n"
            f"  - Captain: {'Yes' if scorer.get('games_captain') else 'No'}\n\n"

            f"**Substitute Stats:**\n"
            f"  - Substitutes In: {scorer.get('substitutes_in', 'N/A')}\n"
            f"  - Substitutes Out: {scorer.get('substitutes_out', 'N/A')}\n"
            f"  - Bench: {scorer.get('substitutes_bench', 'N/A')}\n\n"

            f"**Shooting Stats:**\n"
            f"  - Shots Total: {scorer.get('shots_total', 'N/A')}\n"
            f"  - Shots On Target: {scorer.get('shots_on', 'N/A')}\n\n"

            f"**Goals and Assists:**\n"
            f"  - Goals Scored: {scorer.get('goals_total', 'N/A')}\n"
            f"  - Goals Conceded: {scorer.get('goals_conceded', 'N/A')}\n"
            f"  - Assists: {scorer.get('goals_assists', 'N/A')}\n\n"

            f"**Passing Stats:**\n"
            f"  - Total Passes: {scorer.get('passes_total', 'N/A')}\n"
            f"  - Key Passes: {scorer.get('passes_key', 'N/A')}\n"
            f"  - Passing Accuracy: {scorer.get('passes_accuracy', 'N/A')}\n\n"

            f"**Tackles and Duels:**\n"
            f"  - Tackles Total: {scorer.get('tackles_total', 'N/A')}\n"
            f"  - Duels Total: {scorer.get('duels_total', 'N/A')}\n"
            f"  - Duels Won: {scorer.get('duels_won', 'N/A')}\n\n"

            f"**Dribbling Stats:**\n"
            f"  - Dribbles Attempts: {scorer.get('dribbles_attempts', 'N/A')}\n"
            f"  - Dribbles Success: {scorer.get('dribbles_success', 'N/A')}\n\n"

            f"**Fouls and Cards:**\n"
            f"  - Fouls Drawn: {scorer.get('fouls_drawn', 'N/A')}\n"
            f"  - Fouls Committed: {scorer.get('fouls_committed', 'N/A')}\n"
            f"  - Yellow Cards: {scorer.get('cards_yellow', 'N/A')}\n"
            f"  - Yellow-Red Cards: {scorer.get('cards_yellowred', 'N/A')}\n"
            f"  - Red Cards: {scorer.get('cards_red', 'N/A')}\n\n"

            f"**Penalty Stats:**\n"
            f"  - Penalty Won: {scorer.get('penalty_won', 'N/A')}\n"
            f"  - Penalty Scored: {scorer.get('penalty_scored', 'N/A')}\n"
            f"  - Penalty Missed: {scorer.get('penalty_missed', 'N/A')}\n"
        )
    
    return formatted_output
