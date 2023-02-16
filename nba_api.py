from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import playercareerstats, leaguegamelog
from nba_api.live.nba.endpoints import scoreboard
import pandas as pd

player_dict = players.get_players()
# print(len(player_dict))

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

teams = teams.get_teams()
# print(teams)

seasons = [str(x) + '-' + str(x+1)[-2:] for x in list(range(2020, 2023))]
# print(seasons)
all_league_games = []
for season in seasons:
    league_game = leaguegamelog.LeagueGameLog(season=season).get_data_frames()[0]
    all_league_games.append(league_game)
    # print(league_game)
# print(league_game.get_json())
new_all_league_games = pd.concat(all_league_games)
# print(new_all_league_games)
print(new_all_league_games.head())
print(new_all_league_games.tail())
print(new_all_league_games.columns)