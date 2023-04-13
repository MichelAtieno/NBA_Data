from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import commonplayerinfo ,playercareerstats, playergamelog, leaguegamefinder, boxscorescoringv2, boxscoresummaryv2, boxscoretraditionalv2, playercareerstats, alltimeleadersgrids, teamyearbyyearstats, teamdetails, playerawards, playerdashboardbyyearoveryear, playernextngames, playerprofilev2, scoreboardv2
from nba_api.stats.library.parameters import SeasonAll
from nba_api.live.nba.endpoints import scoreboard
import pandas as pd
import json

#How to get player and team data for team and plaer profiles
#Player Data
player_awards = playerawards.PlayerAwards(player_id="1626164")
player_awards_df = player_awards.get_data_frames()[0]
# print(player_awards_df.columns)

career_stats = playercareerstats.PlayerCareerStats(per_mode36="PerGame", player_id="1626164")
# career_stats = career_stats.career_totals_all_star_season.get_data_frame()
regular_season = career_stats.career_totals_regular_season.get_data_frame()
# print(regular_season)

load_stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id="1626164")
load_stats_df = load_stats.by_year_player_dashboard.get_data_frame()
# load_stats_df =load_stats.overall_player_dashboard.get_data_frame()
# print(load_stats_df)

#How to retrieve log about player from playergamelog endpoint for particular season
gamelog_devbooker = playergamelog.PlayerGameLog(player_id="1626164", season="2022")
gamelog_devbooker_df = gamelog_devbooker.player_game_log.get_data_frame()
# print(gamelog_devbooker_df)
# new_df = gamelog_devbooker_df[["GAME_DATE", "MATCHUP", "PTS", "AST", "MIN", "REB" ]]

next_games = playernextngames.PlayerNextNGames(player_id="1626164")
next_games_df = next_games.next_n_games.get_data_frame()
# print(next_games_df)
# print(next_games_df.columns)

profile = playerprofilev2.PlayerProfileV2(player_id="1626164")
# profile_df = profile.career_highs.get_data_frame()
# profile_df = profile.next_game.get_data_frame()
# profile_df = profile.season_highs.get_data_frame()
# profile_df = profile.season_rankings_post_season.get_data_frame()
# profile_df = profile.season_rankings_regular_season.get_data_frame()
# profile_df = profile.season_totals_post_season.get_data_frame()
# profile_df = profile.season_totals_preseason.get_data_frame()
profile_df = profile.season_totals_regular_season.get_data_frame()
# print(profile_df)
# print(profile_df.columns)

player_dict = players.get_players()
# print(player_dict)
active_players = []
for player in player_dict:
    if player["is_active"] == True:
        active_players.append(player)
# print(active_players)

leaders = alltimeleadersgrids.AllTimeLeadersGrids(topx=30)
# leaders_stats = leaders.ast_leaders.get_data_frame()
leaders_stats = leaders.blk_leaders.get_data_frame()
# print(leaders_stats)



#Team Data
teams = teams.get_teams()
# print(teams)
# all_teams = []
# for team in teams:
#     print(team["id"], team["full_name"])

years = teamyearbyyearstats.TeamYearByYearStats(team_id=1610612756)
years_stats = years.team_stats.get_data_frame()
# print(years_stats)

team_dets = teamdetails.TeamDetails(team_id=1610612756)
# team_dets_df = team_dets.team_awards_championships.get_data_frame()
# team_dets_df = team_dets.team_awards_conf.get_data_frame()
# team_dets_df = team_dets.team_awards_div.get_data_frame()
# team_dets_df = team_dets.team_history.get_data_frame()
# team_dets_df = team_dets.team_background.get_data_frame()
# team_dets_df = team_dets.team_hof.get_data_frame()
team_dets_df = team_dets.team_retired.get_data_frame()
# print(team_dets_df)


#How to retrieve all games from a specific team using leagegamefinder endpoint
phoenix_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=1610612756)
phoenix_games_df = phoenix_games.league_game_finder_results.get_data_frame()
print(phoenix_games_df.head(50))


#BoxScore Details
# box_score = boxscorematchups.BoxScoreMatchups(game_id="")

game_box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id="0022200962")
player_stats = game_box_score.player_stats.get_data_frame()
# print(player_stats)


box_score = boxscoresummaryv2.BoxScoreSummaryV2(game_id="0022200962")
game_info_data = box_score.game_info.get_data_frame()
game_summary_data = box_score.game_summary.get_data_frame()
# print(game_info_data)
# print(game_summary_data)

scoring_data = boxscorescoringv2.BoxScoreScoringV2(game_id="0022200962")
scoring_data_info = scoring_data.get_data_frames()
players_scoring = scoring_data.sql_players_scoring.get_data_frame()

# print(players_scoring)

games = scoreboardv2.ScoreboardV2()
# games_df = games.team_leaders.get_data_frame()
# new_df = games_df[['TEAM_ABBREVIATION',
#         'PTS_PLAYER_NAME', 'PTS',
#        'REB_PLAYER_NAME', 'REB', 'AST_PLAYER_NAME', 'AST']]
# games_df = games.series_standings.get_data_frame()
# games_df = games.east_conf_standings_by_day.get_data_frame()
# games_df = games.west_conf_standings_by_day.get_data_frame()
# games_df = games.line_score.get_data_frame()
# games_df = games.last_meeting.get_data_frame()
# games = scoreboard.ScoreBoard()
games = scoreboardv2.ScoreboardV2()
games = games.get_dict()
games_df = pd.DataFrame([games])
# print(games_df.columns)
# print(games_df[["resultSets"]])
# print(games_df[["parameters"]])
# games_list = games_df.to_dict('records')
# print(games_list)
# games_df = games.get_data_frame()


# print(games_df.columns)










# the_games = leaguegamelog.LeagueGameLog(season="2021-2022", timeout=10).get_data_frames()[0]
# print(the_games)




# print(new_df.head(10))
# first_10 = new_df.head(10)
# # new_dbook_log = new_df.to_csv('new_dbook_log.csv', encoding='utf-8')
# # all_seasons_game_log_list = gamelog_devbooker_df.to_dict('records')
# # print(all_seasons_game_log_list)
# first_10_dbook_log = first_10.to_csv('first_10_log.csv', encoding='utf-8')


# print(gamelog_devbooker_all_df)
# with open("sample.json", "w") as outfile:
#         json.dump(gamelog_devbooker_all_df, outfile)



# print(games_dict)
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

    
