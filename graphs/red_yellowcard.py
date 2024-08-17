import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm
import pandas as pd
import os 

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"/Users/jeevansanchez/create2024/Fifa_world_cup_matches.csv")

font_path = '/Users/jeevansanchez/Downloads/Poppins/Poppins-SemiBold copy.ttf'
prop = fm.FontProperties(fname=font_path)

games_played_team1 = df['team1'].value_counts()
games_played_team2 = df['team2'].value_counts()
games_played = games_played_team1.add(games_played_team2, fill_value=0)

statistic = {team: {'yellow_cards': 0, 'red_cards': 0} for team in df['team1'].unique()}

for i in range(len(df)):
    statistic[df.loc[i, "team1"]]['red_cards'] += df.loc[i, "red cards team1"]
    statistic[df.loc[i, "team2"]]['red_cards'] += df.loc[i, "red cards team2"]
    statistic[df.loc[i, "team1"]]['yellow_cards'] += df.loc[i, "yellow cards team1"]
    statistic[df.loc[i, "team2"]]['yellow_cards'] += df.loc[i, "yellow cards team2"]

joined_stats = pd.DataFrame.from_dict(statistic, orient='index').reset_index()
joined_stats = joined_stats.rename(columns={'index': 'team'})
joined_stats['games_played'] = joined_stats['team'].map(games_played)
data = joined_stats[['yellow_cards', 'red_cards', 'team']]

print(data)

fig, ax1 = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('black')
ax1.set_facecolor('black')

color1 = 'red'
ax1.set_xlabel('Teams', color='white', fontproperties=prop)
ax1.set_ylabel('Red Cards', color=color1, fontproperties=prop, fontsize = '22', labelpad = 25)
ax1.scatter(data['team'], data['red_cards'], color=color1, alpha=0.6, label='Red Cards')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_xticks(range(len(data['team'])))
ax1.set_xticklabels(data['team'], rotation=45, color='white', fontproperties=prop)

ax1.spines['bottom'].set_color('white')
ax1.spines['left'].set_color('white')


color2 = 'yellow'
ax2 = ax1.twinx()
ax2.set_ylabel('Yellow Cards', color=color2, fontproperties=prop, fontsize = '22', labelpad=25)
ax2.scatter(data['team'], data['yellow_cards'], color=color2, marker='o', label='Yellow Cards')
ax2.tick_params(axis='y', labelcolor=color2)

ax2.spines['bottom'].set_color('white')
ax2.spines['left'].set_color('white')


plt.grid(True, linestyle='--', alpha=0.2, color='white')
plt.title("Tournament Red and Yellow Cards", fontproperties=prop, color='white', fontsize = '22')

plot_path = os.path.join("images", "red_yellowcards.png")
plt.savefig(plot_path, facecolor='black')
plt.show()
