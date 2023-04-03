from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import commonplayerinfo ,playercareerstats, leaguegamelog, playergamelog, leaguegamefinder
from nba_api.stats.library.parameters import SeasonAll
from nba_api.live.nba.endpoints import scoreboard
import pandas as pd
import json

#How to get player and team data for team and plaer profiles
#Player Data
player_dict = players.get_players()
# print(player_dict)
active_players = []
for player in player_dict:
    if player["is_active"] == True:
        active_players.append(player)
# print(active_players)
#Team Data
teams = teams.get_teams()
# print(teams)
# all_teams = []
# for team in teams:
#     print(team["id"], team["full_name"])


#How to retrieve log about player from playergamelog endpoint for particular season
gamelog_devbooker = playergamelog.PlayerGameLog(player_id="1626164", season="2022")
gamelog_devbooker_df = gamelog_devbooker.get_data_frames()[0]
new_df = gamelog_devbooker_df[["GAME_DATE", "MATCHUP", "PTS", "AST", "MIN", "REB" ]]
print(new_df.head(10))
first_10 = new_df.head(10)
# new_dbook_log = new_df.to_csv('new_dbook_log.csv', encoding='utf-8')
# all_seasons_game_log_list = gamelog_devbooker_df.to_dict('records')
# print(all_seasons_game_log_list)
first_10_dbook_log = first_10.to_csv('first_10_log.csv', encoding='utf-8')



#How to retrieve log about player's All seasons played by adding SeasonAll parameter
gamelog_devbooker_all = playergamelog.PlayerGameLog(player_id="1626164", season=SeasonAll.all)
gamelog_devbooker_all_df = gamelog_devbooker_all.get_data_frames()[0]
# dbook_log = gamelog_devbooker_all_df.to_csv('dbook_log.csv', encoding='utf-8')

# print(gamelog_devbooker_all_df)
# with open("sample.json", "w") as outfile:
#         json.dump(gamelog_devbooker_all_df, outfile)

#How to retrieve all games from a specific team using leagegamefinder endpoint
phoenix_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=1610612756).get_data_frames()[0]
# print(phoenix_games.head(50))

#How to retrieve game logs from regular season
#You have to specify team_id or player_id
all_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=1610612756, season_nullable="2020-2021", league_id_nullable="00", season_type_nullable="Regular Season")
games = all_games.get_data_frames()[0]
# print(games)


#How to get career stats about player 
career = playercareerstats.PlayerCareerStats(player_id="1626164")
career_stats = career.get_data_frames()[0]
# print(career_stats)

# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]

# json
career.get_json()

# dictionary
career.get_dict()

# print(career.get_json())
# print(career.get_dict())

games = scoreboard.ScoreBoard()
games_dict = games.get_dict()
# print(games_dict)
# for key, value in games_dict.items():
    # print(key)
    # print(value)
    # if key == "scoreboard":
    # #    print(type(value["games"]))
    #    for g in value["games"]:
    #        print(g)   
        # print(len(value["games"]))
        # print(value["games"][0:6])
        # new_list = []
        # some_games = value["games"][0:6]
        # for k in some_games:
        #     for a_key, a_value in k.items():
        #         if a_key not in new_list:
        #             new_list.append(a_key)
                    
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

# How to get player information
player_info = commonplayerinfo.CommonPlayerInfo(player_id="1626164", timeout=100)
player_info = player_info.common_player_info.get_data_frame()
# print(player_info)

# I want to return the score for each player

# On scoreboard data, we can get the game_id
# On player log data we can get game id
# So for example for todays games

#Given scoreboard which has game_id, given player logs which has game_id, map player to a game
# return players associated with scoreboard

# def player_games(player_id):
#     player_games =  playergamelog.PlayerGameLog(player_id=player_id, season="2022").get_data_frames()[0]
#     all_seasons_game_log_list = player_games.to_dict('records')
#     return all_seasons_game_log_list


# def player_scores(game_id):
#     #How to retrieve all games from a specific player 
#     games = scoreboard.ScoreBoard()
#     games_dict = games.get_dict()
#     for key, value in games_dict.items():
#         if key == "scoreboard":
#             for g in value["games"]:
#                 if game_id == g["gameId"]:
#                     return g

    
