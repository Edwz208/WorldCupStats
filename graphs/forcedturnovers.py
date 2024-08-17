# Defensive Pressure Graph

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import matplotlib.font_manager as fm
import os 

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"/Users/jeevansanchez/create2024/Fifa_world_cup_matches.csv")
font_path = '/Users/jeevansanchez/Downloads/Poppins/Poppins-SemiBold copy.ttf'
prop = fm.FontProperties(fname=font_path)


games_played_team1 = df['team1'].value_counts()
games_played_team2 = df['team2'].value_counts()
total_games_played = games_played_team1.add(games_played_team2, fill_value=0)

forced_turnovers = {}
games_played = {}


for i in range(len(df)):
    team1 = df.loc[i, "team1"]
    team2 = df.loc[i, "team2"]

    if team1 not in forced_turnovers:
        forced_turnovers[team1] = 0
        games_played[team1] = 0
    if team2 not in forced_turnovers:
        forced_turnovers[team2] = 0
        games_played[team2] = 0

    forced_turnovers[team1] += df.loc[i, "forced turnovers team1"]
    forced_turnovers[team2] += df.loc[i, "forced turnovers team2"]

    games_played[team1] += 1
    games_played[team2] += 1


df_forced_turnovers = pd.DataFrame.from_dict(forced_turnovers, orient='index', columns=['Forced Turnovers'])
df_games_played = pd.DataFrame.from_dict(games_played, orient='index', columns=['Games Played'])

dfstatistic = df_forced_turnovers.join(df_games_played)
dfstatistic['avg_turnovers'] = dfstatistic['Forced Turnovers'] / dfstatistic['Games Played']

dfstatistic.reset_index(inplace=True)
dfstatistic.rename(columns={"index": "Country"}, inplace=True)

data = dfstatistic[['Country', 'avg_turnovers']]
print(round(data))


plt.figure(figsize=(16,14), facecolor=('black'))
plt.bar(dfstatistic["Country"], dfstatistic['avg_turnovers'], color='#f8f6ee')
plt.xticks(rotation=45, ha='right',  color='#f8f6ee',  fontproperties = prop)
plt.yticks(color='#f8f6ee',  fontproperties = prop)



plt.gca().set_facecolor('black')
plt.title("Tournament Average Forced Turnovers",fontproperties=prop, color='white', fontsize = '22')
plt.xlabel("Teams", fontproperties=prop, color='white', fontsize = '22')
plt.ylabel(" Average Forced Turnovers", fontproperties=prop, color='white', fontsize = '22', labelpad=25)
plt.ylim(bottom = 45)



plot_path = os.path.join("images", "forced_turnovers.png")
plt.savefig(plot_path)
plt.show()