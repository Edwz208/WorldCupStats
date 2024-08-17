import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm

# Set up directories and fonts
os.makedirs("images", exist_ok=True)
font_path = '/Users/jeevansanchez/Downloads/Poppins/Poppins-SemiBold copy.ttf'
prop = fm.FontProperties(fname=font_path)

# Importing the dataset into pandas dataframe
df = pd.read_csv(r"Fifa_world_cup_matches.csv")

x = df.index # Creating a list of the number of rows in dataset

#Country names into a list and statname and value into the dictionary 
# Initialization
countr_names = []
possession = {}
target = {}
forced = {}
scored ={}
conceded = {}
def_pressure = {}
line_breaks = {}
preventions = {}

country_possessions = []
country_target = []
country_forced = []
country_scored = []
country_conceded = []
country_def_pressure = []
country_line_breaks = []
country_preventions = []
df["possession team1"] = df["possession team1"].str.rstrip('%').astype('float')
df["possession team2"] = df["possession team2"].str.rstrip('%').astype('float')
fig, ax = plt.subplots()

# Creating a list of all the countries in the dataset 
for i in range(len(x)):
  if df.loc[i, "team1"] not in countr_names:
    countr_names.append(df.loc[i, "team1"])
    possession[df.loc[i, "team1"]] = 0
    target[df.loc[i, "team1"]] = 0
    forced[df.loc[i, "team1"]] = 0
    line_breaks[df.loc[i, "team1"]] = 0
    def_pressure[df.loc[i, "team1"]] = 0
    scored[df.loc[i, "team1"]] = 0
    conceded[df.loc[i, "team1"]] = 0
    preventions[df.loc[i, "team1"]] = 0
    country_possessions.append(0)
    country_target.append(0)
    country_forced.append(0)
    country_line_breaks.append(0)
    country_def_pressure.append(0)
    country_scored.append(0)
    country_conceded.append(0)
    country_preventions.append(0)
for i in range(len(x)):
  if df.loc[i, "team2"] not in countr_names:
    countr_names.append(df.loc[i, "team2"])
    possession[df.loc[i, "team2"]] = 0
    target[df.loc[i, "team2"]] = 0
    forced[df.loc[i, "team2"]] = 0
    line_breaks[df.loc[i, "team2"]] = 0
    def_pressure[df.loc[i, "team2"]] = 0
    scored[df.loc[i, "team2"]] = 0
    conceded[df.loc[i, "team2"]] = 0
    preventions[df.loc[i, "team2"]] = 0
    country_possessions.append(0)
    country_target.append(0)
    country_forced.append(0)
    country_line_breaks.append(0)
    country_def_pressure.append(0)
    country_scored.append(0)
    country_conceded.append(0)
    country_preventions.append(0)
print(possession)
# Calculating the possession of each country and putting it into the dictionary
for i in range(len(x)):
  possession[df.loc[i, 'team1']]+=df.loc[i, 'possession team1']
  possession[df.loc[i, "team2"]]+=df.loc[i, "possession team2"]
  country_possessions[countr_names.index(df.loc[i,"team1"])] +=1
  country_possessions[countr_names.index(df.loc[i,"team2"])]+=1

  forced[df.loc[i, "team1"]]+=df.loc[i, "forced turnovers team1"]
  forced[df.loc[i, "team2"]]+=df.loc[i, "forced turnovers team2"]
  country_forced[countr_names.index(df.loc[i,"team1"])] +=1
  country_forced[countr_names.index(df.loc[i,"team2"])]+=1

  conceded[df.loc[i, "team1"]]+=df.loc[i, "conceded team1"]
  conceded[df.loc[i, "team2"]]+=df.loc[i, "conceded team2"]
  country_conceded[countr_names.index(df.loc[i,"team1"])] +=1
  country_conceded[countr_names.index(df.loc[i,"team2"])]+=1

  scored[df.loc[i, "team1"]]+=df.loc[i, "number of goals team1"]
  scored[df.loc[i, "team2"]]+=df.loc[i, "number of goals team2"]
  country_scored[countr_names.index(df.loc[i,"team1"])] +=1
  country_scored[countr_names.index(df.loc[i,"team2"])]+=1

  line_breaks[df.loc[i, "team1"]]+=df.loc[i, "completed line breaks team1"]
  line_breaks[df.loc[i, "team2"]]+=df.loc[i, "completed line breaks team2"]
  country_line_breaks[countr_names.index(df.loc[i,"team1"])] +=1
  country_line_breaks[countr_names.index(df.loc[i,"team2"])]+=1

  def_pressure[df.loc[i, "team1"]]+=df.loc[i, "defensive pressures applied team1"]
  def_pressure[df.loc[i, "team2"]]+=df.loc[i, "defensive pressures applied team2"]
  country_def_pressure[countr_names.index(df.loc[i,"team1"])] +=1
  country_def_pressure[countr_names.index(df.loc[i,"team2"])]+=1

  preventions[df.loc[i, "team1"]]+=df.loc[i, "goal preventions team1"]
  preventions[df.loc[i, "team2"]]+=df.loc[i, "goal preventions team2"]
  country_preventions[countr_names.index(df.loc[i,"team1"])] +=1
  country_preventions[countr_names.index(df.loc[i,"team2"])]+=1

  target[df.loc[i, "team1"]]+=df.loc[i, "on target attempts team1"]
  target[df.loc[i, "team2"]]+=df.loc[i, "on target attempts team2"]
  country_target[countr_names.index(df.loc[i,"team1"])] +=1
  country_target[countr_names.index(df.loc[i,"team2"])]+=1


# Average possession calculated
for i in range(len(countr_names)):
  possession[countr_names[i]] /= country_possessions[i]
  forced[countr_names[i]] /= country_forced[i]
  scored[countr_names[i]] /= country_scored[i]
  preventions[countr_names[i]] /= country_preventions[i]
  def_pressure[countr_names[i]] /= country_def_pressure[i]
  conceded[countr_names[i]] /= country_conceded[i]
  target[countr_names[i]] /= country_target[i]
  line_breaks[countr_names[i]] /= country_line_breaks[i]


metrics_first = {
    'Country Name': countr_names[0],
    'Ball Possession (%)': possession[countr_names[0]],
    'Shots On Target (#)': target[countr_names[0]],
    'Forced Turnovers (#)': forced[countr_names[0]],
    'Conceded Goals (#)': conceded[countr_names[0]],
    'Goals Scored (#)': scored[countr_names[0]],
    'Goals Prevented (#)': preventions[countr_names[0]],
    'Defensive Line Breaks (#)': line_breaks[countr_names[0]],
    'Defensive Pressures Applied (#)': def_pressure[countr_names[0]]
}
# Create DataFrame
updateddf = pd.DataFrame([metrics_first])
del possession[countr_names[0]]
del target[countr_names[0]]
del forced[countr_names[0]]
del conceded[countr_names[0]]
del scored[countr_names[0]]
del preventions[countr_names[0]]
del line_breaks[countr_names[0]]
del def_pressure[countr_names[0]]
del [countr_names[0]]
for i in range(len(countr_names)):  # Iterate over indices
    metrics = {
        'Country Name': countr_names[i],
        'Ball Possession (%)': possession[countr_names[i]],
        'Shots On Target (#)': target[countr_names[i]],
        'Forced Turnovers (#)': forced[countr_names[i]],
        'Conceded Goals (#)': conceded[countr_names[i]],
        'Goals Scored (#)': scored[countr_names[i]],
        'Goals Prevented (#)': preventions[countr_names[i]],
        'Defensive Line Breaks (#)': line_breaks[countr_names[i]],
        'Defensive Pressures Applied (#)': def_pressure[countr_names[i]]
    }
    df_dictionary = pd.DataFrame([metrics])
    updateddf = pd.concat([updateddf, df_dictionary], ignore_index=True)
print(updateddf)
# Converting the dictionary into another dataframe
# Depugging
normalized_df = pd.DataFrame()
normalized_df["Country Name"] = updateddf["Country Name"]
normalized_df["Country Name"] = updateddf["Country Name"]

target_min, target_max = 0.5, 1

# Mean normalization function for columns
def mean_normalize_column(column, reverse=False):
    mean_val = updateddf[column].mean()
    min_val = updateddf[column].min()
    max_val = updateddf[column].max()

    if reverse:
        return target_max - ((updateddf[column] - mean_val) / (max_val - min_val)) * 0.5
    else:
        return target_min + ((updateddf[column] - mean_val) / (max_val - min_val)) * 0.5

metrics_list = [
  'Ball Possession (%)', 'Shots On Target (#)', 'Forced Turnovers (#)', 
  'Conceded Goals (#)', 'Goals Scored (#)', 'Goals Prevented (#)', 
  'Defensive Line Breaks (#)', 'Defensive Pressures Applied (#)'
]
for column in metrics_list:
  if "conceded" in column:
      normalized_df[column] = mean_normalize_column(column, reverse=True)
  else:
      normalized_df[column] = mean_normalize_column(column)

print(normalized_df)

france_df = normalized_df[normalized_df['Country Name'] == 'FRANCE']

def plot_radar_chart(data, metricsfun, title):
    N = len(metricsfun)
    theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
    theta = np.concatenate([theta, [theta[0]]])

    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw={'projection': 'polar'}, facecolor = 'black')

    ax.set_title(title, y=1.15, fontsize=20)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(90)
    ax.spines['polar'].set_zorder(1)
    ax.spines['polar'].set_color('lightgrey')
    ax.spines(alpha = 0.3)

    # Use straight quotation marks in color_palette
    color_palette = ['#830c8e', '#0500FF', '#9CDADB', '#FF00DE', '#FF9900', '#FFFFFF']

    for idx, (i, row) in enumerate(data.iterrows()):
        values = row[metricsfun].values.flatten().tolist()
        values = values + [values[0]]
        ax.plot(theta, values, linewidth=1.75, linestyle='solid', label=row['Country Name'], marker='o', markersize=10, color=color_palette[idx % len(color_palette)])
        ax.fill(theta, values, alpha=0.50, color=color_palette[idx % len(color_palette)])

    # Correct the y-ticks and x-ticks
    plt.yticks([0, 0.25, 0.5, 0.75, 1], ["","","","",""], color="white", size=12,)
    plt.xticks(theta[:-1], metricsfun, color='white', size=12)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1)) 
    plt.gca().set_facecolor('black')
    plt.title("France Tournament Performance", color='white', fontsize = 30, pad=45, fontproperties = prop)

    return fig

fig = plot_radar_chart(france_df, metrics_list, title="Soccer Radar Chart")
plot_path = os.path.join("images", "france_spider.png")
plt.savefig(plot_path)
plt.show()