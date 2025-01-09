def format_match_statistics_data(match_statistics_data):
    
    formatted_output = "**Match Statistics Data**\n"

    for match in match_statistics_data:
        fixture_id = match.get('fixture_id', 'N/A')
        team_id = match.get('team_id', 'N/A')
        statistics = match.get('statistics', {})

        if statistics:
            formatted_output += (
                f"\n**Fixture ID:** {fixture_id}\n"
                f"**Team ID:** {team_id}\n"
                f"**Team Name:** {statistics.get('team_name', 'N/A')}\n"
                f"**Team Logo:** {statistics.get('team_logo', 'N/A')}\n\n"

                f"**Shooting Statistics:**\n"
                f"  - Shots on Goal: {statistics.get('Shots on Goal', 'N/A')}\n"
                f"  - Shots off Goal: {statistics.get('Shots off Goal', 'N/A')}\n"
                f"  - Total Shots: {statistics.get('Total Shots', 'N/A')}\n"
                f"  - Blocked Shots: {statistics.get('Blocked Shots', 'N/A')}\n"
                f"  - Shots Inside Box: {statistics.get('Shots insidebox', 'N/A')}\n"
                f"  - Shots Outside Box: {statistics.get('Shots outsidebox', 'N/A')}\n\n"

                f"**Fouls and Corners:**\n"
                f"  - Fouls: {statistics.get('Fouls', 'N/A')}\n"
                f"  - Corner Kicks: {statistics.get('Corner Kicks', 'N/A')}\n"
                f"  - Offsides: {statistics.get('Offsides', 'N/A')}\n\n"

                f"**Possession and Passing:**\n"
                f"  - Ball Possession: {statistics.get('Ball Possession', 'N/A')}\n"
                f"  - Total Passes: {statistics.get('Total passes', 'N/A')}\n"
                f"  - Passes Accurate: {statistics.get('Passes accurate', 'N/A')}\n"
                f"  - Pass Accuracy: {statistics.get('Passes %', 'N/A')}\n\n"

                f"**Card Statistics:**\n"
                f"  - Yellow Cards: {statistics.get('Yellow Cards', 'N/A')}\n"
                f"  - Red Cards: {statistics.get('Red Cards', 'N/A')}\n\n"

                f"**Goalkeeper Statistics:**\n"
                f"  - Goalkeeper Saves: {statistics.get('Goalkeeper Saves', 'N/A')}\n"
            )
        else:

            formatted_output += f"\nNo statistics data available for fixture {fixture_id} and team {team_id}\n"

    return formatted_output


#testing
#if __name__ == "__main__":
    sample_data = [
        {
            'fixture_id': 718729,
            'team_id': 85,
            'statistics': {
                'team_name': 'Paris Saint Germain',
                'team_logo': 'https://media.api-sports.io/football/teams/85.png',
                'Shots on Goal': 12,
                'Shots off Goal': 10,
                'Total Shots': 27,
                'Blocked Shots': 5,
                'Shots insidebox': 20,
                'Shots outsidebox': 7,
                'Fouls': 7,
                'Corner Kicks': 4,
                'Offsides': 2,
                'Ball Possession': '75%',
                'Total passes': 761,
                'Passes accurate': 699,
                'Passes %': '92%',
                'Yellow Cards': 1,
                'Red Cards': 0,
                'Goalkeeper Saves': 1
            }
        },
        {
            'fixture_id': 718709,
            'team_id': 85,
            'statistics': {}
        }
    ]
    formatted_output = format_match_statistics_data(sample_data)
    print(formatted_output)
