import matplotlib.pyplot as plt 
import pandas as pd
import os 
import matplotlib.font_manager as fm

# Create directory for images if it doesn't exist
os.makedirs("images", exist_ok=True)

# Load data
df = pd.read_csv("/Users/jeevansanchez/create2024/Fifa_world_cup_matches.csv")

# Set custom font properties
font_path = '/Users/jeevansanchez/Downloads/Poppins/Poppins-SemiBold copy.ttf'
prop = fm.FontProperties(fname=font_path)

# Initialize dictionaries
games_played = {}
goals_scored = {}

# Aggregate games played and goals scored
for i in range(len(df)):
    team1 = df.loc[i, "team1"]
    team2 = df.loc[i, "team2"]
    
    # Update games played
    if team1 in games_played:
        games_played[team1] += 1
    else:
        games_played[team1] = 1
        
    if team2 in games_played:
        games_played[team2] += 1
    else:
        games_played[team2] = 1
        
    # Update goals scored
    goals_scored[team1] = goals_scored.get(team1, 0) + df.loc[i, "number of goals team1"]
    goals_scored[team2] = goals_scored.get(team2, 0) + df.loc[i, "number of goals team2"]

# Create DataFrames
df_goals_scored = pd.DataFrame.from_dict(goals_scored, orient='index', columns=['Goals Scored'])
df_games_played = pd.DataFrame.from_dict(games_played, orient='index', columns=['Games Played'])
df_statistic = df_goals_scored.join(df_games_played)

# Calculate average goals scored
df_statistic['Average Goals Scored'] = df_statistic['Goals Scored'] / df_statistic['Games Played']

# Prepare data for plotting
df_statistic.reset_index(inplace=True)
df_statistic.rename(columns={"index": "Country"}, inplace=True)

# Plotting
plt.figure(figsize=(16, 14), facecolor='black')
plt.bar(df_statistic["Country"], df_statistic["Average Goals Scored"], color='#f8f6ee')
plt.xticks(rotation=45, ha='right', color='#f8f6ee', fontproperties=prop, )
plt.yticks(color='#f8f6ee', fontproperties=prop)

plt.gca().set_facecolor('black')
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['left'].set_color('white')

plt.title("Tournament Average Goals Scored", fontproperties=prop, color='white', fontsize=22)
plt.xlabel("Teams", fontproperties=prop, color='white', fontsize=22, labelpad=25)
plt.ylabel("Average Goals Scored", fontproperties=prop, color='white', fontsize=22, labelpad=25)

# Save and show plot
plot_path = os.path.join("images", "goals-scored.png")
plt.savefig(plot_path)
plt.show()
