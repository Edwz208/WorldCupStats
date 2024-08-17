import matplotlib.pyplot as plt 
import pandas as pd
import os 
import matplotlib.font_manager as fm

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"/Users/jeevansanchez/create2024/Fifa_world_cup_matches.csv")

font_path = '/Users/jeevansanchez/Downloads/Poppins/Poppins-SemiBold copy.ttf'
prop = fm.FontProperties(fname=font_path)


x = df.index
countr_names = []
statistic = {}


for i in range(len(x)):
  if df.loc[i, "team1"] not in countr_names:
    countr_names.append(df.loc[i, "team1"])
    statistic[df.loc[i, "team1"]] = 0
for i in range(len(x)):
  if df.loc[i, "team2"] not in countr_names:
    countr_names.append(df.loc[i, "team2"])
    statistic[df.loc[i, "team2"]] = 0

for i in range(len(x)):
   statistic[df.loc[i, "team1"]]+=df.loc[i, "penalties scored team1"]
   statistic[df.loc[i, "team2"]]+=df.loc[i, "penalties scored team2"]

   
  
cols = ['statName']


statistic = pd.DataFrame.from_dict(statistic, orient='index', columns=cols)
y_statistic = statistic["statName"]
statistic.reset_index(inplace=True)
statistic.rename(columns={"index": "Country"}, inplace=True)
x_statistic = []


for i in range(len(y_statistic)):
  x_statistic.append(i)
print(y_statistic)
print(len(y_statistic))

print(len(x_statistic))

plt.figure(figsize=(16,14), facecolor='black')
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['left'].set_color('white')

plt.bar(statistic["Country"],y_statistic, color = '#f8f6ee')
plt.xticks(color='white', fontsize=12, rotation = 45, fontproperties = prop)
plt.yticks(color='white', fontsize=12)

plt.gca().set_facecolor('black')
plt.title("Tournament Penalties Scored", fontproperties=prop, color='white', fontsize = '22')
plt.ylabel("Penalties Scored", fontproperties = prop, fontsize = 22, color = 'white', labelpad= 25)
plt.xlabel("Teams", fontproperties = prop, fontsize = 22, color = 'white', labelpad=25)



plot_path = os.path.join("images", "penalties.png")
plt.savefig(plot_path)

plt.show()