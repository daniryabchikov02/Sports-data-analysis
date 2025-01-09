def format_injuries_for_chatgpt(injuries_data):

    formatted_output = "**Injury Report for Fixture**\n\n"
    
    if not injuries_data:
        return formatted_output + "No injury data available.\n"
    
    for injury in injuries_data:
        formatted_output += (
            f"**Player:** {injury['player_name']}\n"
            f"  - Photo: {injury['player_photo']}\n"
            f"  - Injury Type: {injury['injury_type']}\n"
            f"  - Reason: {injury['injury_reason']}\n"
            f"  - Team: {injury['team_name']} (Logo: {injury['team_logo']})\n"
            f"  - Fixture Date: {injury['fixture_date']}\n"
            f"  - League: {injury['league_name']} (Logo: {injury['league_logo']})\n\n"
        )
    
    return formatted_output

if __name__ == "__main__":

    injuries_data = [
        {'player_name': 'D. Costa', 'player_photo': 'https://media.api-sports.io/football/players/865.png', 'injury_type': 'Missing Fixture', 'injury_reason': 'Broken ankle', 'team_name': 'Bayern Munich', 'team_logo': 'https://media.api-sports.io/football/teams/157.png', 'fixture_date': '2021-04-07T19:00:00+00:00', 'league_name': 'UEFA Champions League', 'league_logo': 'https://media.api-sports.io/football/leagues/2.png'}
        
    ]
    
    print(format_injuries_for_chatgpt(injuries_data))
