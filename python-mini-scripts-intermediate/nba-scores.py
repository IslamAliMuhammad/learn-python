from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data["links"]
    return links

def get_current_scoreboard():
    link = get_links()["currentScoreboard"]
    games = get(BASE_URL + link).json()["games"]

    for game in games:
        home_team = game["hTeam"]
        away_team = game["vTeam"]
        
        print(f"{home_team['triCode']} VS {away_team['triCode']} \n {home_team['score']} {away_team['score']}")
        print(f"{game['clock']} - {game['period']['current']}")
        print("_______________________________________________________")

# get_current_scoreboard()

def get_stats():
    links = get_links()
    data = get(BASE_URL + links["leagueTeamStatsLeaders"]).json()
    teams = data["league"]["standard"]['preseason']["teams"]
    
    teams.sort(key=lambda x: int(x['ppg']['rank']))
    
    for i, team in enumerate(teams):
        name = team["name"]
        nickname = team["nickname"]
        ppg = team["ppg"]["avg"]
        
        print(f"{i + 1}. {name} - {nickname} - {ppg}")
        
get_stats()
        
    
    