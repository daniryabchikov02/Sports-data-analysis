from datetime import datetime, timedelta, timezone
from api_files.fixtures_fetcher import get_upcoming_fixtures
from config import LEAGUE_ID, SEASON

def process_fixtures_data(fixtures_data=None, manual_date=None):
    
    if fixtures_data is None:
        fixtures_data = get_upcoming_fixtures()

    today = manual_date.astimezone(timezone.utc) if manual_date else datetime.now(timezone.utc)
    date_limit = today + timedelta(weeks=2)

    print(f"Manual test date (UTC): {today}")
    print(f"Date limit (2 weeks from test date): {date_limit}")

    upcoming_fixtures = []

    for fixture in fixtures_data.get("response", []):

        fixture_date_str = fixture["fixture"]["date"]
        try:
            fixture_date = datetime.fromisoformat(fixture_date_str.replace("Z", "+00:00")).astimezone(timezone.utc)
        except ValueError as e:
            print(f"Error parsing date for fixture ID {fixture['fixture']['id']}: {e}")
            continue

        if today <= fixture_date <= date_limit:

            fixture_info = {
                "fixture_id": fixture["fixture"]["id"],
                "league_id": fixture["league"]["id"],
                "league_name": fixture["league"]["name"],
                "home_team_id": fixture["teams"]["home"]["id"],
                "home_team_name": fixture["teams"]["home"]["name"],
                "away_team_id": fixture["teams"]["away"]["id"],
                "away_team_name": fixture["teams"]["away"]["name"],
                "date": fixture_date_str,  
                "season": fixture["league"].get("season", None)
            }
            upcoming_fixtures.append(fixture_info)

    return upcoming_fixtures

#testing
#if __name__ == "__main__":
#    fixtures_data = get_upcoming_fixtures()
#    manual_date = datetime(2021, 10, 10, tzinfo=timezone.utc)
#    upcoming_fixtures = process_fixtures_data(fixtures_data, manual_date=manual_date)
