import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm
import os

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"/Users/jeevansanchez/create2024/Fifa_world_cup_matches.csv")

font_path = '/Users/jeevansanchez/Downloads/Poppins/Poppins-SemiBold copy.ttf'
prop = fm.FontProperties(fname=font_path)

statistic = {team: {'on_target': 0, 'off_target': 0} for team in pd.concat([df['team1'], df['team2']]).unique()}

for i in range(len(df)):
    statistic[df.loc[i, "team1"]]['on_target'] += df.loc[i, "on target attempts team1"]
    statistic[df.loc[i, "team2"]]['on_target'] += df.loc[i, "on target attempts team2"]
    statistic[df.loc[i, "team1"]]['off_target'] += df.loc[i, "off target attempts team1"]
    statistic[df.loc[i, "team2"]]['off_target'] += df.loc[i, "off target attempts team2"]

joined_stats = pd.DataFrame.from_dict(statistic, orient='index').reset_index()
joined_stats = joined_stats.rename(columns={'index': 'team'})
print(joined_stats)

plt.figure(figsize=(20, 16), facecolor='black')
plt.scatter(joined_stats['off_target'], joined_stats['on_target'], color='#d41de5', label='Shots On Target', s=100, edgecolors='black', alpha=0.75)

plt.gca().set_facecolor('black')
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['left'].set_color('white')

plt.title("Tournament Shot Accuracy", fontproperties=prop, color='white', fontsize = '22')
plt.xlabel("Shots Off Target", fontproperties=prop, color='white', fontsize = '22', labelpad= 25)
plt.ylabel("Shots On Target", fontproperties=prop, color='white', fontsize = '22', labelpad= 25)

plt.xticks(color='white', fontsize=12)
plt.yticks(color='white', fontsize=12)

plt.xlim(0, joined_stats['off_target'].max() + 10)
plt.ylim(0, joined_stats['on_target'].max() + 10)

plt.grid(True, linestyle='--', alpha=0.3)

top_teams = joined_stats.nlargest(31, 'on_target')
for i, row in top_teams.iterrows():
    team_abbreviation = row['team'][:3].upper()  
    plt.annotate(team_abbreviation, (row['off_target'], row['on_target']),
                 textcoords="offset points", xytext=(10, 10), ha='center', color='white', fontsize=10, fontproperties = prop)
    


plot_path = os.path.join("images", "shotson_shotsoff.png")
plt.savefig(plot_path)
plt.show()
