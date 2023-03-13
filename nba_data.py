from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import playercareerstats, leaguegamelog, playergamelog, leaguegamefinder
from nba_api.stats.library.parameters import SeasonAll
from nba_api.live.nba.endpoints import scoreboard
import pandas as pd

#How to get player and team data for team and plaer profiles
#Player Data
player_dict = players.get_players()
# print(player_dict)
active_players = []
for player in player_dict:
    if player["is_active"] == True:
        active_players.append(player)

#Team Data
teams = teams.get_teams()
# print(teams)
all_teams = []
for team in teams:
    print(team["id"], team["full_name"])


#How to retrieve log about player from playergamelog endpoint for particular season
gamelog_devbooker = playergamelog.PlayerGameLog(player_id="1626164", season="2022")
gamelog_devbooker_df = gamelog_devbooker.get_data_frames()[0]
# print(gamelog_devbooker_df)

#How to retrieve log about player's All seasons played by adding SeasonAll parameter
gamelog_devbooker_all = playergamelog.PlayerGameLog(player_id="1626164", season=SeasonAll.all)
gamelog_devbooker_all_df = gamelog_devbooker_all.get_data_frames()[0]
# print(gamelog_devbooker_all_df)

#How to retrieve all games from a specific team using leagegamefinder endpoint
Phoenix_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=1610612756).get_data_frames()[0]
print(Phoenix_games.columns)


career = playercareerstats.PlayerCareerStats(player_id="203999")
# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]

# json
career.get_json()

# dictionary
career.get_dict()

# print(career)
# print(career.get_data_frames()[0])
# print(career.get_json())
# print(career.get_dict())

games = scoreboard.ScoreBoard()
games_dict = games.get_dict()
for key, value in games_dict.items():
    # # print(key)
    # print(value)
    if key == "scoreboard":
        # print(value["gameDate"])
        # print(len(value["games"]))
        # print(value["games"][0:6])
        new_list = []
        some_games = value["games"][0:6]
        for k in some_games:
            for a_key, a_value in k.items():
                if a_key not in new_list:
                    new_list.append(a_key)
                    
        # print(new_list)

# print(games)
# print(type(games.get_dict()))



# seasons = [str(x) + '-' + str(x+1)[-2:] for x in list(range(2020, 2023))]
# # print(seasons)
# all_league_games = []
# for season in seasons:
#     league_game = leaguegamelog.LeagueGameLog(season=season).get_data_frames()[0]
#     all_league_games.append(league_game)
#     # print(league_game)
# # print(league_game.get_json())
# new_all_league_games = pd.concat(all_league_games)
# # print(new_all_league_games)
# print(new_all_league_games.head())
# print(new_all_league_games.tail())
# print(new_all_league_games.columns)