import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from copy import deepcopy
from time import sleep, time

# URLs of Top 5 European Leagues, the second string is concatenated with the season and
# stat we are looking for
LEAGUE_URLS = {
    "Premier League": ["https://fbref.com/en/comps/9/","/Premier-League-Stats"],
    "Bundesliga": ["https://fbref.com/en/comps/20/","/Bundesliga-Stats"],
    "LaLiga": ["https://fbref.com/en/comps/12/","/La-Liga-Stats"],
    "Serie A": ["https://fbref.com/en/comps/11/","/Serie-A-Stats"],
    "Ligue 1": ["https://fbref.com/en/comps/13/", "/Ligue-1-Stats"]
}

STATS = {
    "stats": ['team', 'players_used', 'avg_age', 'possession', 'games', 'games_starts', 'minutes', 'minutes_90s', 'goals', 'assists', 'goals_assists', 'goals_pens', 'pens_made', 'pens_att', 'cards_yellow', 'cards_red', 'xg', 'npxg', 'xg_assist', 'npxg_xg_assist', 'progressive_carries', 'progressive_passes', 'goals_per90', 'assists_per90', 'goals_assists_per90', 'goals_pens_per90', 'goals_assists_pens_per90', 'xg_per90', 'xg_assist_per90', 'xg_xg_assist_per90', 'npxg_per90', 'npxg_xg_assist_per90'],
    "keepers": ['players_used', 'gk_games', 'gk_games_starts', 'gk_minutes', 'minutes_90s', 'gk_goals_against', 'gk_goals_against_per90', 'gk_shots_on_target_against', 'gk_saves', 'gk_save_pct', 'gk_wins', 'gk_ties', 'gk_losses', 'gk_clean_sheets', 'gk_clean_sheets_pct', 'gk_pens_att', 'gk_pens_allowed', 'gk_pens_saved', 'gk_pens_missed', 'gk_pens_save_pct'],
    "keepersadv": ['gk_goals_against', 'gk_pens_allowed', 'gk_free_kick_goals_against', 'gk_corner_kick_goals_against', 'gk_own_goals_against', 'gk_psxg', 'gk_psnpxg_per_shot_on_target_against', 'gk_psxg_net', 'gk_psxg_net_per90', 'gk_passes_completed_launched', 'gk_passes_launched', 'gk_passes_pct_launched', 'gk_passes', 'gk_passes_throws', 'gk_pct_passes_launched', 'gk_passes_length_avg', 'gk_goal_kicks', 'gk_pct_goal_kicks_launched', 'gk_goal_kick_length_avg', 'gk_crosses', 'gk_crosses_stopped', 'gk_crosses_stopped_pct', 'gk_def_actions_outside_pen_area', 'gk_def_actions_outside_pen_area_per90', 'gk_avg_distance_def_actions'],
    "shooting":['goals', 'shots', 'shots_on_target', 'shots_on_target_pct', 'shots_per90', 'shots_on_target_per90', 'goals_per_shot', 'goals_per_shot_on_target', 'average_shot_distance', 'shots_free_kicks', 'pens_made', 'pens_att', 'xg', 'npxg', 'npxg_per_shot', 'xg_net', 'npxg_net'],
    "passing": ['passes_completed', 'passes', 'passes_pct', 'passes_total_distance', 'passes_progressive_distance', 'passes_completed_short', 'passes_short', 'passes_pct_short', 'passes_completed_medium', 'passes_medium', 'passes_pct_medium', 'passes_completed_long', 'passes_long', 'passes_pct_long', 'assists', 'xg_assist', 'pass_xa', 'xg_assist_net', 'assisted_shots', 'passes_into_final_third', 'passes_into_penalty_area', 'crosses_into_penalty_area', 'progressive_passes'],
    "passing_types": ['passes', 'passes_live', 'passes_dead', 'passes_free_kicks', 'through_balls', 'passes_switches', 'crosses', 'throw_ins', 'corner_kicks', 'corner_kicks_in', 'corner_kicks_out', 'corner_kicks_straight', 'passes_completed', 'passes_offsides', 'passes_blocked'],
    "gca": ['sca', 'sca_per90', 'sca_passes_live', 'sca_passes_dead', 'sca_take_ons', 'sca_shots', 'sca_fouled', 'sca_defense', 'gca', 'gca_per90', 'gca_passes_live', 'gca_passes_dead', 'gca_take_ons', 'gca_shots', 'gca_fouled', 'gca_defense'],
    "defense": ['tackles', 'tackles_won', 'tackles_def_3rd', 'tackles_mid_3rd', 'tackles_att_3rd', 'challenge_tackles', 'challenges', 'challenge_tackles_pct', 'challenges_lost', 'blocks', 'blocked_shots', 'blocked_passes', 'interceptions', 'tackles_interceptions', 'clearances', 'errors'],
    "possession": ['possession', 'minutes_90s', 'touches', 'touches_def_pen_area', 'touches_def_3rd', 'touches_mid_3rd', 'touches_att_3rd', 'touches_att_pen_area', 'touches_live_ball', 'take_ons', 'take_ons_won', 'take_ons_won_pct', 'take_ons_tackled', 'take_ons_tackled_pct', 'carries', 'carries_distance', 'carries_progressive_distance', 'progressive_carries', 'carries_into_final_third', 'carries_into_penalty_area', 'miscontrols', 'dispossessed', 'passes_received', 'progressive_passes_received'],
    "playingtime":['avg_age', 'games', 'minutes', 'minutes_per_game', 'minutes_pct', 'minutes_90s', 'games_starts', 'minutes_per_start', 'games_complete', 'games_subs', 'minutes_per_sub', 'unused_subs', 'points_per_game', 'on_goals_for', 'on_goals_against', 'plus_minus', 'plus_minus_per90', 'on_xg_for', 'on_xg_against', 'xg_plus_minus', 'xg_plus_minus_per90'],
    "misc": ['cards_yellow', 'cards_red', 'cards_yellow_red', 'fouls', 'fouled', 'offsides', 'crosses', 'interceptions', 'tackles_won', 'pens_won', 'pens_conceded', 'own_goals', 'ball_recoveries', 'aerials_won', 'aerials_lost', 'aerials_won_pct']
}

class RateLimiter:
    def __init__(self, max_requests, period, sleep_time):
        self.max_requests = max_requests
        self.period = period
        self.sleep_time = sleep_time
        self.requests = []
    
    def wait(self):
        current_time = time()
        self.requests = [req for req in self.requests if current_time - req < self.period]
        if len(self.requests) >= self.max_requests:
            print(f"Rate limit reached. Sleeping for {self.sleep_time:.2f} seconds...")
            sleep(self.sleep_time)
        self.requests.append(time())
        sleep(2)  # Sleep 1 second between each request

rate_limiter = RateLimiter(max_requests=14, period=60, sleep_time=90)

def categoryFrame(category, url):
    """Returns a dataframe of a given category"""
    def getTable(url):
        """Returns the table containing team stats"""
        rate_limiter.wait()
        res = requests.get(url)
        print(f"Fetching URL: {url}")
        print(f"Response status code: {res.status_code}")
        comm = re.compile("<!--|-->")
        soup = BeautifulSoup(comm.sub("", res.text), "lxml")
        allTables = soup.findAll("tbody")
        print(f"Found {len(allTables)} tables")
        if len(allTables) == 0:
            print("Error: No tables found.")
            return None
        teamTable = allTables[0]
        return teamTable

    def getFrame(category, teamTable):
        """Returns a dataframe of a given category, from the
        table containing team stats"""
        dfDict = {}
        features = STATS[category]
        rows = teamTable.find_all("tr")
        for row in rows:
            if row.find("th", {"scope": "row"}):
                for f in features:
                    if f == 'team':
                        cell = row.find("th", {"data-stat": "team"})
                        if cell:
                            text = " ".join(cell.text.strip().encode().decode("utf-8").split(" "))
                        else:
                            text = ''
                    else:
                        cell = row.find("td", {"data-stat": f})
                        if not cell:
                            text = ''
                        else:
                            text = cell.text.strip().encode().decode("utf-8")
                            if "," in str(text):
                                text = int(text.replace(",", ""))
                    if (text == ''):
                        text = 0
                    if f in dfDict:
                        dfDict[f].append(text)
                    else:
                        dfDict[f] = [text]
        dfTeam = pd.DataFrame.from_dict(dfDict)
        return dfTeam

    url = url[0] + category + url[1]
    teamTable = getTable(url)
    if teamTable is None:
        return pd.DataFrame()
    dfTeam = getFrame(category, teamTable)
    return dfTeam

def getTeamData(url):
    """Returns a dataframe of all stats for teams in the league"""
    dfStats = categoryFrame("stats", url)
    dfKeepers = categoryFrame("keepers", url)
    dfKeepersAdv = categoryFrame("keepersadv", url)
    dfShooting = categoryFrame("shooting", url)
    dfPassing = categoryFrame("passing", url)
    dfPassingTypes = categoryFrame("passing_types", url)
    dfGCA = categoryFrame("gca", url)
    dfDefense = categoryFrame("defense", url)
    dfPossession = categoryFrame("possession", url)
    dfMisc = categoryFrame("misc", url)
    df = pd.concat([dfStats, dfKeepers, dfKeepersAdv, dfShooting, dfPassing, dfPassingTypes, dfGCA, dfDefense, dfPossession, dfMisc], axis=1)
    df = df.loc[:, ~df.columns.duplicated()]
    return df

class FBrefScraper:
    def __init__(self, leagues, seasons):
        self.leagues = leagues
        self.seasons = seasons

    def scrapeTeams(self, csvPath=None):
        """Returns a dataframe of all stats for teams in the leagues"""
        teamStats = pd.DataFrame()

        for season in self.seasons:
            for league in self.leagues:
                print(f"Scraping {league}, {season - 1}/{season}...")

                url = deepcopy(LEAGUE_URLS[league])
                if 'Big5' not in url[0]:
                    url[0] = f"{url[0]}{season - 1}-{season}/"
                    url[1] = f"/{season - 1}-{season}-{url[1]}"
                dfSeason = getTeamData(url)
                dfSeason["season"] = season
                dfSeason["league"] = league
                teamStats = teamStats._append(dfSeason, ignore_index=True)

        if csvPath:
            teamStats.to_csv(csvPath, index=False)
        return teamStats

# Example usage
if __name__ == "__main__":
    scraper = FBrefScraper(["Premier League", "Bundesliga", "LaLiga","Serie A", "Ligue 1"], [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017])
    scraper.scrapeTeams("data/top5Leagues.csv")