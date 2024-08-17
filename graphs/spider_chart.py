import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r"/Users/jeevansanchez/create2024/Fifa_world_cup_matches.csv")

df["possession team1"] = df["possession team1"].str.rstrip('%').astype('float')
df["possession team2"] = df["possession team2"].str.rstrip('%').astype('float')

argentina_df = df[(df['team1'] == 'Argentina') | (df['team2'] == 'ARGENTINA')]
games_played_argentina = len(argentina_df)

possession = 0
ontarget = 0
forced_turnovers = 0
conceded = 0
goals_scored = 0
preventions = 0
defensive_pressures = 0
line_breaks = 0

for index, row in argentina_df.iterrows():
    if row['team1'] == 'ARGENTINA':
        possession += row["possession team1"]
        ontarget += row["on target attempts team1"]
        forced_turnovers += row["forced turnovers team1"]
        conceded += row["conceded team1"]
        goals_scored += row["number of goals team1"]
        preventions += row["goal preventions team1"]
        line_breaks += row["completed defensive line breaks team1"]
        defensive_pressures += row["defensive pressures applied team1"]
    elif row['team2'] == 'ARGENTINA':  # Argentina is team2
        possession += row["possession team2"]
        ontarget += row["on target attempts team2"]
        forced_turnovers += row["forced turnovers team2"]
        conceded += row["conceded team2"]
        goals_scored += row["number of goals team2"]
        preventions += row["goal preventions team2"]
        line_breaks += row["completed defensive line breaks team2"]
        defensive_pressures += row["defensive pressures applied team2"]

def avg_stat(total, games_played):
    return round(total / games_played, 2)


avg_possession = avg_stat(possession, games_played_argentina)
avg_ontarget = avg_stat(ontarget, games_played_argentina)
avg_forced_turnovers = avg_stat(forced_turnovers, games_played_argentina)
avg_conceded = avg_stat(conceded, games_played_argentina)
avg_goals = avg_stat(goals_scored, games_played_argentina)
avg_preventions = avg_stat(preventions, games_played_argentina)
avg_linebreaks = avg_stat(line_breaks, games_played_argentina)
avg_defensivepressures = avg_stat(defensive_pressures, games_played_argentina)

# Print results for Argentina
# print("\nArgentina Statistics:")
# print(f"Average Possession: {avg_possession}%")
# print(f"Average On Target Attempts: {avg_ontarget}")
# print(f"Average Forced Turnovers: {avg_forced_turnovers}")
# print(f"Average Conceded Goals: {avg_conceded}")
# print(f"Average Goals Scored: {avg_goals}")
# print(f"Average Goals Prevented: {avg_preventions}")
# print(f"Average Defensive Line Breaks: {avg_linebreaks}")
# print(f"Average Defensive Pressures Applied: {avg_defensivepressures}")

metrics_averages = {
    'Ball Possession': avg_possession,
    'Shots On Target': avg_ontarget,
    'Forced Turnovers': avg_forced_turnovers,
    'Conceded Goals': avg_conceded,
    'Goals Scored': avg_goals,
    'Goals Prevented': avg_preventions,
    'Defensive Line Breaks': avg_linebreaks,
    'Defensive Pressures Applied': avg_defensivepressures
}

print("Metrics and Averages:")
for metric, avg in metrics_averages.items():
    print(f"{metric}: {avg}")




