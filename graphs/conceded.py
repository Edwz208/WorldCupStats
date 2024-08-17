import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib.font_manager as fm

# Create directory for saving images if it doesn't exist
os.makedirs("images", exist_ok=True)

# Load the dataset
df = pd.read_csv("Fifa_world_cup_matches.csv")

# Font properties
font_path = '/Users/jeevansanchez/Downloads/Poppins/Poppins-SemiBold copy.ttf'
prop = fm.FontProperties(fname=font_path)

# Calculate total goals conceded and games played for each team
statistic = {}
games_played = {}

for i in range(len(df)):
    team1 = df.loc[i, "team1"]
    team2 = df.loc[i, "team2"]
    conceded1 = df.loc[i, "conceded team1"]
    conceded2 = df.loc[i, "conceded team2"]
    
    if team1 in statistic:
        statistic[team1] += conceded1
    else:
        statistic[team1] = conceded1
        
    if team2 in statistic:
        statistic[team2] += conceded2
    else:
        statistic[team2] = conceded2
        
    if team1 in games_played:
        games_played[team1] += 1
    else:
        games_played[team1] = 1
        
    if team2 in games_played:
        games_played[team2] += 1
    else:
        games_played[team2] = 1

# Calculate average goals conceded per game
for team in statistic:
    statistic[team] /= games_played[team]

# Convert to DataFrame for plotting
df_statistic = pd.DataFrame({'Country': list(statistic.keys()), 'Average Goals Conceded': list(statistic.values())})

# Plotting

plt.figure(figsize=(14, 10), facecolor= 'black')
plt.bar(df_statistic['Country'], df_statistic['Average Goals Conceded'], color='#f8f6ee')
plt.xticks(rotation=45, fontsize=12, fontproperties=prop, color='white')
plt.yticks(color='white', fontsize=12)
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['left'].set_color('white')
plt.gca().set_facecolor('black')
plt.title("Average Goals Conceded per Team", fontproperties=prop, fontsize=22, color='white')
plt.xlabel("Teams", fontproperties=prop, fontsize=22, color='white')
plt.ylabel("Average Goals Conceded", fontproperties=prop, fontsize=22, color='white')

# Save and display plot
plot_path = os.path.join("images", "conceded.png")
plt.savefig(plot_path)
plt.show()
