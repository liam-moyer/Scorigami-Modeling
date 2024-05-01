#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('pip install selenium')


# In[9]:


get_ipython().system('pip install html5lib')


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import csv
from selenium import webdriver
import html5lib
import datetime as dt
import random


# In[73]:


# MORE DATA SCRAPING (ADDING 2022-2023 SEASON)

teams = ['giants', 'bears', 'bengals', 'browns', 'packers', 'titans', 'dolphins', 'washington', 'panthers', 'jaguars', 
      'broncos', 'raiders', 'buccaneers', 'texans', 'patriots', 'falcons', 'cowboys', 'colts', 'chiefs', 'saints', 'jets', 
      'ravens', 'rams', 'seahawks', 'vikings', 'chargers', '49ers', 'steelers', 'eagles', 'cardinals', 'lions']

team = 'bills'
driver = webdriver.Chrome()
driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-game-in-2022")
driver.implicitly_wait(5)
html = driver.page_source
driver.implicitly_wait(5)
tables = pd.read_html(html)
nfl_games = tables[0]
driver.close()

count=0
for team in teams:
    driver = webdriver.Chrome()
    driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-game-in-2022")

    # import random and use random number between 7 and 12
    driver.implicitly_wait(5)

    html = driver.page_source

    # import random and use random number between 7 and 12
    driver.implicitly_wait(5)
    
    tables = pd.read_html(html)
    nfl_games = pd.concat([nfl_games, tables[0]])
    count += 1
    
    if (nfl_games.columns.tolist() != tables[0].columns.tolist()):
        print("Columns do not match.")

    driver.close()


# In[74]:


# Add Season

df = pd.read_csv("RegSeasonNFLGameData(1994-2023).csv")

year=2023
season = []

for index, row in df.iterrows():
    
    if (row['TEAM'] == 'Buffalo Bills' and row['WEEK']==0):
        year-=1          
    season.append(year)

df['SEASON'] = season
df.to_csv('RegSeasonNFLGameData(1994-2023).csv')


# In[75]:


df = pd.read_csv("RegSeasonNFLGameData(1994-2023).csv")

td, pass_td, rush_td, ret_td, fg, xp, xp2, sfty = 0, 0, 0, 0, 0, 0, 0, 0
avg_td, avg_pass_td, avg_rush_td, avg_ret_td, avg_fg, avg_xp, avg_xp2, avg_sfty = {}, {}, {}, {}, {}, {}, {}, {}

drow = 2022
for index, row in df.iterrows():
    
    if (row['SEASON'] < drow):
        
        avg_td[row['SEASON']]=td/(len(df[(df['SEASON'] == drow)]))
        avg_pass_td[row['SEASON']]=pass_td/(len(df[(df['SEASON'] == drow)]))
        avg_rush_td[row['SEASON']]=rush_td/(len(df[(df['SEASON'] == drow)]))
        avg_ret_td[row['SEASON']]=ret_td/(len(df[(df['SEASON'] == drow)]))
        avg_fg[row['SEASON']]=fg/(len(df[(df['SEASON'] == drow)]))
        avg_xp[row['SEASON']]=xp/(len(df[(df['SEASON'] == drow)]))
        avg_xp2[row['SEASON']]=xp2/(len(df[(df['SEASON'] == drow)]))
        avg_sfty[row['SEASON']]=sfty/(len(df[(df['SEASON'] == drow)]))
        td, pass_td, rush_td, ret_td, fg, xp, xp2, sfty = 0, 0, 0, 0, 0, 0, 0, 0
        drow=row['SEASON']
        
    td+=row['TD']
    pass_td+=row['PASS TD']
    rush_td+=row['RUSH TD']
    ret_td+=row['RET TD']
    fg+=row['FGM']
    xp+=row['XPM']
    xp2+=row['XP2']
    sfty+=row['SFTY']

# dict_list = [avg_td, avg_pass_td, avg_rush_td, avg_ret_td, avg_fg, avg_xp, avg_xp2, avg_sfty]
# avg_scores = pd.DataFrame.from_dict(dict_list)
# avg_scores.to_csv('AvgScores.csv')

# print(avg_scores)
    
epoch1 = [1994, 2014]
epoch2 = [2015, 2022]

e1td, e1pass_td, e1rush_td, e1ret_td, e1fg, e1xp, e1xp2, e1sfty = 0, 0, 0, 0, 0, 0, 0, 0
epoch1_df = df[(df['SEASON'] >= (epoch1[0])) & (df['SEASON'] <= (epoch1[1]))]
for index, row in epoch1_df.iterrows():
    e1td+=row['TD']
    e1pass_td+=row['PASS TD']
    e1rush_td+=row['RUSH TD']
    e1ret_td+=row['RET TD']
    e1fg+=row['FGM']
    e1xp+=row['XPM']
    e1xp2+=row['XP2']
    e1sfty+=row['SFTY']

e1td=e1td/(len(epoch1_df))
e1pass_td=e1pass_td/(len(epoch1_df))
e1rush_td=e1rush_td/(len(epoch1_df))
e1ret_td=e1ret_td/(len(epoch1_df))
e1fg=e1fg/(len(epoch1_df))
e1xp=e1xp/(len(epoch1_df))
e1xp2=e1xp2/(len(epoch1_df))
e1sfty=e1sfty/(len(epoch1_df))

    
e2td, e2pass_td, e2rush_td, e2ret_td, e2fg, e2xp, e2xp2, e2sfty = 0, 0, 0, 0, 0, 0, 0, 0
epoch2_df = df[(df['SEASON'] >= (epoch2[0])) & (df['SEASON'] <= (epoch2[1]))]

for index, row in epoch1_df.iterrows():
    e2td+=row['TD']
    e2pass_td+=row['PASS TD']
    e2rush_td+=row['RUSH TD']
    e2ret_td+=row['RET TD']
    e2fg+=row['FGM']
    e2xp+=row['XPM']
    e2xp2+=row['XP2']
    e2sfty+=row['SFTY']

e2td=e2td/(len(epoch2_df))
e2pass_td=e2pass_td/(len(epoch2_df))
e2rush_td=e2rush_td/(len(epoch2_df))
e2ret_td=e2ret_td/(len(epoch2_df))
e2fg=e2fg/(len(epoch2_df))
e2xp=e2xp/(len(epoch2_df))
e2xp2=e2xp2/(len(epoch2_df))
e2sfty=e2sfty/(len(epoch2_df))


# In[76]:


# Plotting Reg Season

plt.ylabel("Num of Touchdowns")
plt.xlabel("Season")
plt.title("Number of Touchdowns per Team per Game per Season (1994-2023)")
plt.plot(avg_td.keys(), avg_td.values())
plt.show()

plt.ylabel("Num of FG")
plt.xlabel("Season")
plt.title("Number of FG's per Team per Game per Season (1994-2023)")
plt.plot(avg_fg.keys(), avg_fg.values())
plt.show()

plt.ylabel("Num of Pass TD")
plt.xlabel("Season")
plt.title("Number of Pass TD per Team per Game per Season (1994-2023)")
plt.plot(avg_pass_td.keys(), avg_pass_td.values())
plt.show()

plt.ylabel("Num of Rush TD")
plt.xlabel("Season")
plt.title("Number of Rush TD per Team per Game per Season (1994-2023)")
plt.plot(avg_rush_td.keys(), avg_rush_td.values())
plt.show()

plt.ylabel("Num of Extra Points")
plt.xlabel("Season")
plt.title("Number of Extra Points per Team per Game per Season (1994-2023)")
plt.plot(avg_xp.keys(), avg_xp.values())
plt.show()

plt.ylabel("Num of Two Point Conversions")
plt.xlabel("Season")
plt.title("Number of Two Point Conversions per Team per Game per Season (1994-2023)")
plt.plot(avg_xp2.keys(), avg_xp2.values())
plt.show()

plt.ylabel("Num of Safeties")
plt.xlabel("Season")
plt.title("Number of Safeties per Team per Game per Season (1994-2023)")
plt.plot(avg_xp2.keys(), avg_xp2.values())
plt.show()


# In[3]:


# MORE DATA SCRAPING (ADDING 2022-2023 PLAYOFFS)

teams = ['giants', 'bears', 'bengals', 'browns', 'packers', 'titans', 'dolphins', 'washington', 'panthers', 'jaguars', 
      'broncos', 'raiders', 'buccaneers', 'texans', 'patriots', 'falcons', 'cowboys', 'colts', 'chiefs', 'saints', 'jets', 
      'ravens', 'rams', 'seahawks', 'vikings', 'chargers', '49ers', 'steelers', 'eagles', 'cardinals', 'lions']

team = 'bills'
driver = webdriver.Chrome()
driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-playoff-game-in-2022")
driver.implicitly_wait(5)
html = driver.page_source
driver.implicitly_wait(5)
tables = pd.read_html(html)
nfl_playoff_games = tables[0]
driver.close()


count = 0

for team in teams:
    driver = webdriver.Chrome()
    driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-playoff-game-in-2022")

    driver.implicitly_wait(5)

    html = driver.page_source

    driver.implicitly_wait(5)
    try:
        # check that the columns in tables[0] match the columns in nfl_playoff_games
        tables = pd.read_html(html)
        nfl_playoff_games = pd.concat([nfl_playoff_games, tables[0]])
        count += 1
        if (nfl_playoff_games.columns.tolist() != tables[0].columns.tolist()):
            print("Columns do not match.")
    except ValueError:
        continue
        
    driver.close()
    
#nfl_playoff_games.to_csv('PlayoffNFLGameData(1994-2023).csv')


# In[6]:


# PLAYOFF

df = pd.read_csv("PlayoffNFLGameData(1994-2023).csv")

td, pass_td, rush_td, ret_td, fg, xp, xp2, sfty = 0, 0, 0, 0, 0, 0, 0, 0
avg_td, avg_pass_td, avg_rush_td, avg_ret_td, avg_fg, avg_xp, avg_xp2, avg_sfty = {}, {}, {}, {}, {}, {}, {}, {}

drow = 2022
for index, row in df.iterrows():
    
    if (row['SEASON'] < drow):
        
        avg_td[row['SEASON']]=td/(len(df[(df['SEASON'] == drow)]))
        avg_pass_td[row['SEASON']]=pass_td/(len(df[(df['SEASON'] == drow)]))
        avg_rush_td[row['SEASON']]=rush_td/(len(df[(df['SEASON'] == drow)]))
        avg_ret_td[row['SEASON']]=ret_td/(len(df[(df['SEASON'] == drow)]))
        avg_fg[row['SEASON']]=fg/(len(df[(df['SEASON'] == drow)]))
        avg_xp[row['SEASON']]=xp/(len(df[(df['SEASON'] == drow)]))
        avg_xp2[row['SEASON']]=xp2/(len(df[(df['SEASON'] == drow)]))
        avg_sfty[row['SEASON']]=sfty/(len(df[(df['SEASON'] == drow)]))
        td, pass_td, rush_td, ret_td, fg, xp, xp2, sfty = 0, 0, 0, 0, 0, 0, 0, 0
        drow=row['SEASON']
        
    td+=row['TD']
    pass_td+=row['PASS TD']
    rush_td+=row['RUSH TD']
    ret_td+=row['RET TD']
    fg+=row['FGM']
    xp+=row['XPM']
    xp2+=row['XP2']
    sfty+=row['SFTY']

# dict_list = [avg_td, avg_pass_td, avg_rush_td, avg_ret_td, avg_fg, avg_xp, avg_xp2, avg_sfty]
# avg_scores = pd.DataFrame.from_dict(dict_list)
# avg_scores.to_csv('AvgScores.csv')

# print(avg_scores)
    
epoch1 = [1994, 2014]
epoch2 = [2015, 2022]

e1td, e1pass_td, e1rush_td, e1ret_td, e1fg, e1xp, e1xp2, e1sfty = 0, 0, 0, 0, 0, 0, 0, 0
epoch1_df = df[(df['SEASON'] >= (epoch1[0])) & (df['SEASON'] <= (epoch1[1]))]
for index, row in epoch1_df.iterrows():
    e1td+=row['TD']
    e1pass_td+=row['PASS TD']
    e1rush_td+=row['RUSH TD']
    e1ret_td+=row['RET TD']
    e1fg+=row['FGM']
    e1xp+=row['XPM']
    e1xp2+=row['XP2']
    e1sfty+=row['SFTY']

e1td=e1td/(len(epoch1_df))
e1pass_td=e1pass_td/(len(epoch1_df))
e1rush_td=e1rush_td/(len(epoch1_df))
e1ret_td=e1ret_td/(len(epoch1_df))
e1fg=e1fg/(len(epoch1_df))
e1xp=e1xp/(len(epoch1_df))
e1xp2=e1xp2/(len(epoch1_df))
e1sfty=e1sfty/(len(epoch1_df))

    
e2td, e2pass_td, e2rush_td, e2ret_td, e2fg, e2xp, e2xp2, e2sfty = 0, 0, 0, 0, 0, 0, 0, 0
epoch2_df = df[(df['SEASON'] >= (epoch2[0])) & (df['SEASON'] <= (epoch2[1]))]

for index, row in epoch1_df.iterrows():
    e2td+=row['TD']
    e2pass_td+=row['PASS TD']
    e2rush_td+=row['RUSH TD']
    e2ret_td+=row['RET TD']
    e2fg+=row['FGM']
    e2xp+=row['XPM']
    e2xp2+=row['XP2']
    e2sfty+=row['SFTY']

e2td=e2td/(len(epoch2_df))
e2pass_td=e2pass_td/(len(epoch2_df))
e2rush_td=e2rush_td/(len(epoch2_df))
e2ret_td=e2ret_td/(len(epoch2_df))
e2fg=e2fg/(len(epoch2_df))
e2xp=e2xp/(len(epoch2_df))
e2xp2=e2xp2/(len(epoch2_df))
e2sfty=e2sfty/(len(epoch2_df))



# In[7]:


# Plotting Playoff

plt.ylabel("Num of Touchdowns")
plt.xlabel("Season")
plt.title("Number of Touchdowns per Team per Playoff Game per Season (1994-2023)")
plt.plot(avg_td.keys(), avg_td.values())
plt.show()

plt.ylabel("Num of FG")
plt.xlabel("Season")
plt.title("Number of FG's per Team per Playoff Game per Season (1994-2023)")
plt.plot(avg_fg.keys(), avg_fg.values())
plt.show()

plt.ylabel("Num of Pass TD")
plt.xlabel("Season")
plt.title("Number of Pass TD per Team per PLayoff Game per Season (1994-2023)")
plt.plot(avg_pass_td.keys(), avg_pass_td.values())
plt.show()

plt.ylabel("Num of Rush TD")
plt.xlabel("Season")
plt.title("Number of Rush TD per Team per Playoff Game per Season (1994-2023)")
plt.plot(avg_rush_td.keys(), avg_rush_td.values())
plt.show()

plt.ylabel("Num of Extra Points")
plt.xlabel("Season")
plt.title("Number of Extra Points per Team per Playoff Game per Season (1994-2023)")
plt.plot(avg_xp.keys(), avg_xp.values())
plt.show()

plt.ylabel("Num of Two Point Conversions")
plt.xlabel("Season")
plt.title("Number of Two Point Conversions per Team per Playoff Game per Season (1994-2023)")
plt.plot(avg_xp2.keys(), avg_xp2.values())
plt.show()

plt.ylabel("Num of Safeties")
plt.xlabel("Season")
plt.title("Number of Safeties per Team per Playoff Game per Season (1994-2023)")
plt.plot(avg_xp2.keys(), avg_xp2.values())
plt.show()


# In[19]:


# ADD ALL GAMES

df = pd.read_csv("AllNFLTeams.csv")
teams = {}

# for index, row in df.iterrows():
#     teams[row['TEAM']]=''
    
for index, row in df.iterrows():
    if (len(row['YEARS'])==4):
        teams[row['TEAM']]=[row['YEARS']]
    else:
        year_range = row['YEARS'].split('-')
        teams[row['TEAM']]=year_range

print(teams)

print(type(teams))

del teams['Washington Redskins']
del teams['Los Angeles Rams']
del teams['St. Louis Rams']
teams['Washington']=['1932', '2022']
teams['Rams']=['1937', '2022']


# In[57]:


import random

team = 'Buffalo Bills'

driver = webdriver.Chrome()
driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-playoff-game-in-2022")
driver.implicitly_wait(5)
html = driver.page_source
tables = pd.read_html(html)
driver.implicitly_wait(5)
nfl_games = tables[0]
    
for year in range(1961, 1999):
    driver = webdriver.Chrome()
    driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-playoff-game-in-" +str(year))
    time=random.SystemRandom().uniform(1, 3)
    driver.implicitly_wait(time)
    html = driver.page_source
    driver.implicitly_wait(time)
    try:
        tables = pd.read_html(html)
        nfl_games = pd.concat([nfl_games, tables[0]])
        #count += 1
        if (nfl_games.columns.tolist() != tables[0].columns.tolist()):
            print("Columns do not match.")    
    except ValueError:
        continue

team_list = list(teams.keys())
team_list.remove('Buffalo Bills')

problems = []

for team in team_list:
    
    if ((len(teams[team]))==1):
        start=int(teams[team][0])
        end=int(teams[team][0])
    else:
        start=int(teams[team][0])
        end=int(teams[team][1])
    
    if (end>1998):
        end=1998
    
    for year in range(start, end+1):
        
        driver = webdriver.Chrome()
        driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-playoff-game-in-" + str(year) + "nfl")
        time=random.SystemRandom().uniform(1, 3)

        # import random and use random number between 7 and 12
        driver.implicitly_wait(time)

        html = driver.page_source

        # import random and use random number between 7 and 12
        driver.implicitly_wait(time)
    
        try:
            tables = pd.read_html(html)
            nfl_games = pd.concat([nfl_games, tables[0]])
            #count += 1
    
            if (nfl_games.columns.tolist() != tables[0].columns.tolist()):
                print("Columns do not match.")
                problems.append(str(team)+ " "+ str(year))
                
                
        except ValueError:
            continue

        driver.close()
        
nfl_games.to_csv('RESCRAPE_PLAYOFF.csv')


# In[53]:


print(nfl_games)


# In[16]:


print(problems)


# In[7]:





# In[3]:


nfl_games.drop_duplicates()
nfl_games.to_csv('ALL_DATA_1920-1994.csv')

new_df_test = nfl_games

new_df_test.sort_values(by='DATE')
nfl_games.to_csv('ALLDATATEST.csv')


# In[113]:


# Add Season For ALL GAMES

df = pd.read_csv('NFLGameData(RegSeason1920-2023).csv')
df = df.drop_duplicates()

d_year=2023
season = []


for index, row in df.iterrows():
    
    
    row['DATE'] = pd.to_datetime(row['DATE'])
    year = row['DATE'].year
    
    if (row['WEEK']==0 and year > d_year):
        d_year=year
        year-=1
    season.append(year)

df['SEASON'] = season
df.to_csv('NFLGameData(RegSeason1920-2023).csv')

print(df)


# In[95]:


#Scorigami Distributions Through Different Epochs
df = pd.read_csv("EveryScorigami.csv")

epoch1 = "1920-1933"
epoch2 = "1934-1948"
epoch3 = "1949-1973"
epoch4 = "1974-1993"
epoch5 = "1994-2015"
epoch6 = "2016-2022"

epoch_list=[epoch1, epoch2, epoch3, epoch4, epoch5, epoch6]

scorigami_epoch = {}

for x in epoch_list:
    scorigami_epoch[x]=0

for index, row in df.iterrows():
    if (row['New Scorigami?']==True):
        if (row['Season'] >= 1920 and row['Season']<=1933):
            scorigami_epoch[epoch1]+=1
        elif (row['Season'] >= 1933 and row['Season']<=1948):
            scorigami_epoch[epoch2]+=1
        elif (row['Season'] >= 1949 and row['Season']<=1973):
            scorigami_epoch[epoch3]+=1
        elif (row['Season'] >= 1974 and row['Season']<=1993):
            scorigami_epoch[epoch4]+=1
        elif (row['Season'] >= 1994 and row['Season']<=2015):
            scorigami_epoch[epoch5]+=1
        else:
            scorigami_epoch[epoch6]+=1

print(scorigami_epoch)

plt.ylabel("Number of New Scorigamis")
plt.xlabel("Seasons")
plt.title("Number of Scorigamis per Epoch")
plt.plot(scorigami_epoch.keys(), scorigami_epoch.values())
plt.show()


# In[ ]:


# COMBINE DATA

df = pd.read_csv("NFLGameData(RegSeason1920-2023)")

td, pass_td, rush_td, ret_td, fg, xp, xp2, sfty = 0, 0, 0, 0, 0, 0, 0, 0
avg_td, avg_pass_td, avg_rush_td, avg_ret_td, avg_fg, avg_xp, avg_xp2, avg_sfty = {}, {}, {}, {}, {}, {}, {}, {}

drow = 2022
for index, row in df.iterrows():
    
    if (row['SEASON'] < drow):
        
        avg_td[row['SEASON']]=td/(len(df[(df['SEASON'] == drow)]))
        avg_pass_td[row['SEASON']]=pass_td/(len(df[(df['SEASON'] == drow)]))
        avg_rush_td[row['SEASON']]=rush_td/(len(df[(df['SEASON'] == drow)]))
        avg_ret_td[row['SEASON']]=ret_td/(len(df[(df['SEASON'] == drow)]))
        avg_fg[row['SEASON']]=fg/(len(df[(df['SEASON'] == drow)]))
        avg_xp[row['SEASON']]=xp/(len(df[(df['SEASON'] == drow)]))
        avg_xp2[row['SEASON']]=xp2/(len(df[(df['SEASON'] == drow)]))
        avg_sfty[row['SEASON']]=sfty/(len(df[(df['SEASON'] == drow)]))
        td, pass_td, rush_td, ret_td, fg, xp, xp2, sfty = 0, 0, 0, 0, 0, 0, 0, 0
        drow=row['SEASON']
        
    td+=row['TD']
    pass_td+=row['PASS TD']
    rush_td+=row['RUSH TD']
    ret_td+=row['RET TD']
    fg+=row['FGM']
    xp+=row['XPM']
    xp2+=row['XP2']
    sfty+=row['SFTY']

# dict_list = [avg_td, avg_pass_td, avg_rush_td, avg_ret_td, avg_fg, avg_xp, avg_xp2, avg_sfty]
# avg_scores = pd.DataFrame.from_dict(dict_list)
# avg_scores.to_csv('AvgScores1920-2023.csv')

# print(avg_scores)
    
epoch1 = "1920-1933"
epoch2 = "1934-1948"
epoch3 = "1949-1973"
epoch4 = "1974-1993"
epoch5 = "1994-2015"
epoch6 = "2016-2022"

epoch_list=[epoch1, epoch2, epoch3, epoch4, epoch5, epoch6]

epoch_avg_td = {}
epoch_avg_pass_td = {}
epoch_avg_rush_td = {}
epoch_avg_ret_td = {}
epoch_avg_fg = {}
epoch_avg_xp = {}
epoch_avg_xp2 = {}
epoch_avg_sfty = {}

for x in epoch_list:
    epoch_avg_td[x] = 0
    epoch_avg_pass_td[x] = 0
    epoch_avg_rush_td[x] = 0
    epoch_avg_ret_td[x] = 0
    epoch_avg_fg[x] = 0
    epoch_avg_xp[x] = 0
    epoch_avg_xp2[x] = 0
    epoch_avg_sfty[x] = 0


for index, row in epoch1_df.iterrows():
    if(row['SEASON'] >= 1920 and row['SEASON'] <= 1933):
        years="1920-1933"
    elif (row['SEASON'] >= 1934 and row['SEASON'] <= 1948):
        years="1934-1948"
    elif (row['SEASON'] >= 1949 and row['SEASON'] <= 1973):
        years="1949-1973"
    elif (row['SEASON'] >= 1974 and row['SEASON'] <= 1993):
        years="1974-1993"
    elif (row['SEASON'] >= 1994 and row['SEASON'] <= 2015):
        years="1994-2015"
    elif (row['SEASON'] >= 2016 and row['SEASON'] <= 2022):
        years="2016-2022"
        
    epoch_avg_td[years]+=row['TD']
    epoch_avg_pass_td[years]+=row['PASS TD']
    epoch_avg_rush_td[years]+=row['RUSH TD']
    epoch_avg_ret_td[years]+=row['RET TD']
    epoch_avg_fg[years]+=row['FGM']
    epoch_avg_xp[years]+=row['XPM']
    epoch_avg_xp2[years]+=row['XP2']
    epoch_avg_sfty[years]+=row['SFTY']
    

epoch_avg_td[years]=row['TD']
epoch_avg_pass_td[years]=row['PASS TD']
epoch_avg_rush_td[years]=row['RUSH TD']
epoch_avg_ret_td[years]=row['RET TD']
epoch_avg_fg[years]+=row['FGM']
epoch_avg_xp[years]+=row['XPM']
epoch_avg_xp2[years]+=row['XP2']
epoch_avg_sfty[years]+=row['SFTY']


# In[35]:


# SCRAPE PROBLEM TEAMS

team = 'Patriots'

driver = webdriver.Chrome()
driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-" + team + "-have-in-each-game-in-1950-nfl")
driver.implicitly_wait(5)
html = driver.page_source
tables = pd.read_html(html)
driver.implicitly_wait(5)
nfl_games = tables[0]


for year in range(1950, 1951):
    driver = webdriver.Chrome()
    driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-New-York-Yanks-have-in-each-game-in-" +str(year)+"-nfl")
    time=random.SystemRandom().uniform(1, 3)
    driver.implicitly_wait(time)
    html = driver.page_source
    driver.implicitly_wait(time)
    try:
        tables = pd.read_html(html)
        nfl_games = pd.concat([nfl_games, tables[0]])
        #count += 1
        if (nfl_games.columns.tolist() != tables[0].columns.tolist()):
            print("Columns do not match.")    
    except ValueError:
        continue

print(nfl_games)
nfl_games.to_csv('NewYorkYanks1951.csv')


# In[19]:


nfl_games.to_csv('ProblemTeams.csv')


# In[25]:


import datetime as dt

problem_teams = pd.read_csv('ProblemTeams.csv')

print(problem_teams)
for index, row in df.iterrows():
    
    print(row['TEAM'])
    row['DATE'] = pd.to_datetime(row['DATE'])
    year = row['DATE'].year
    row['SEASON']=year
    
problem_teams.to_csv('UPADTED-ProblemTeams.csv')


# In[74]:


df = pd.read_csv("NFLGameData(RegSeason1940-2023).csv")

epoch1 = "1940-1955"
epoch2 = "1956-1973"
epoch3 = "1974-1993"
epoch4 = "1994-2015"
epoch5 = "2016-2022"


epoch_list=[epoch1, epoch2, epoch3, epoch4, epoch5]

epoch_avg_td = {}
epoch_avg_pass_td = {}
epoch_avg_rush_td = {}
epoch_avg_ret_td = {}
epoch_avg_fg = {}
epoch_avg_xp = {}
epoch_avg_xp2 = {}
epoch_avg_sfty = {}

for x in epoch_list:
    epoch_avg_td[x] = 0
    epoch_avg_pass_td[x] = 0
    epoch_avg_rush_td[x] = 0
    epoch_avg_ret_td[x] = 0
    epoch_avg_fg[x] = 0
    epoch_avg_xp[x] = 0
    epoch_avg_xp2[x] = 0
    epoch_avg_sfty[x] = 0


for index, row in df.iterrows():
    if(row['SEASON'] >= 1940 and row['SEASON'] <= 1955):
        years="1940-1955"
    elif (row['SEASON'] >= 1956 and row['SEASON'] <= 1973):
        years="1956-1973"
    elif (row['SEASON'] >= 1974 and row['SEASON'] <= 1993):
        years="1974-1993"
    elif (row['SEASON'] >= 1994 and row['SEASON'] <= 2015):
        years="1994-2015"
    elif (row['SEASON'] >= 2016 and row['SEASON'] <= 2022):
        years="2016-2022"
        
    epoch_avg_td[years]+=row['TD']
    epoch_avg_pass_td[years]+=row['PASS TD']
    epoch_avg_rush_td[years]+=row['RUSH TD']
    epoch_avg_ret_td[years]+=row['RET TD']
    epoch_avg_fg[years]+=row['FGM']
    epoch_avg_xp[years]+=row['XPM']
    epoch_avg_xp2[years]+=row['XP2']
    epoch_avg_sfty[years]+=row['SFTY']
    

for years in epoch_list: 
    
    year_list=years.split('-')
    start=year_list[0]
    end=year_list[1]
    
    
    new_df = df[(df['SEASON'] >= int(start)) & (df['SEASON'] <= int(end))]
    
    epoch_avg_td[years]=epoch_avg_td[years]/len(new_df)
    epoch_avg_pass_td[years]=epoch_avg_pass_td[years]/len(new_df)
    epoch_avg_rush_td[years]=epoch_avg_rush_td[years]/len(new_df)
    epoch_avg_ret_td[years]= epoch_avg_ret_td[years]/len(new_df)
    epoch_avg_fg[years]=epoch_avg_fg[years]/len(new_df)
    epoch_avg_xp[years]=epoch_avg_xp[years]/len(new_df)
    epoch_avg_xp2[years]=epoch_avg_xp2[years]/len(new_df)
    epoch_avg_sfty[years]=epoch_avg_sfty[years]/len(new_df)
    
    
    
    


# In[71]:


# Plotting 1940-2023 Averages

plt.ylabel("Num of Touchdowns")
plt.xlabel("Season")
plt.title("Number of Touchdowns per Team per Game per Season (1940-2023)")
plt.plot(epoch_avg_td.keys(), epoch_avg_td.values())
plt.show()

plt.ylabel("Num of FG")
plt.xlabel("Season")
plt.title("Number of FG's per Team per Game per Season (1940-2023)")
plt.plot(epoch_avg_fg.keys(), epoch_avg_fg.values())
plt.show()

plt.ylabel("Num of Pass TD")
plt.xlabel("Season")
plt.title("Number of Pass TD per Team per Game per Season (1940-2023)")
plt.plot(epoch_avg_pass_td.keys(), epoch_avg_pass_td.values())
plt.show()

plt.ylabel("Num of Rush TD")
plt.xlabel("Season")
plt.title("Number of Rush TD per Team per Playoff Game per Season (1940-2023)")
plt.plot(epoch_avg_rush_td.keys(), epoch_avg_rush_td.values())
plt.show()

plt.ylabel("Num of Extra Points")
plt.xlabel("Season")
plt.title("Number of Extra Points per Team per Game per Season (1940-2023)")
plt.plot(epoch_avg_xp.keys(), epoch_avg_xp.values())
plt.show()

plt.ylabel("Num of Two Point Conversions")
plt.xlabel("Season")
plt.title("Number of Two Point Conversions per Team per Game per Season (1940-2023)")
plt.plot(epoch_avg_xp2.keys(), epoch_avg_xp2.values())
plt.show()

plt.ylabel("Num of Safeties")
plt.xlabel("Season")
plt.title("Number of Safeties per Team per Game per Season (1940-2023)")
plt.plot(epoch_avg_sfty.keys(), epoch_avg_sfty.values())
plt.show()


# In[104]:


# Box Plot

df = pd.read_csv("NFLGameData(RegSeason1940-2023).csv")

epoch1 = "1940-1955"
epoch2 = "1956-1973"
epoch3 = "1974-1993"
epoch4 = "1994-2015"
epoch5 = "2016-2022"

epoch_list=[epoch1, epoch2, epoch3, epoch4, epoch5]

e1_frame = df[(df['SEASON'] >= 1940) & (df['SEASON'] <= 1955)]
e2_frame = df[(df['SEASON'] >= 1956) & (df['SEASON'] <= 1973)]
e3_frame = df[(df['SEASON'] >= 1974) & (df['SEASON'] <= 1993)]
e4_frame = df[(df['SEASON'] >= 1994) & (df['SEASON'] <= 2015)]
e5_frame = df[(df['SEASON'] >= 2016) & (df['SEASON'] <= 2022)]


e1_td = e1_frame['TD']
e2_td = e2_frame['TD']
e3_td = e3_frame['TD']
e4_td = e4_frame['TD']
e5_td = e5_frame['TD']
plt.title('Average Touchdowns per Team per Game per Epoch')
plt.ylabel('Number of Touchdowns')
plt.xlabel('Epochs')
plt.boxplot ([e1_td, e2_td, e3_td, e4_td, e5_td])
plt.xticks([1, 2, 3, 4, 5], ["1940-1955", "1956-1973", "1974-1993", "1994-2015", "2016-2022"])
plt.show()


e1_pass = e1_frame['PASS TD']
e2_pass = e2_frame['PASS TD']
e3_pass = e3_frame['PASS TD']
e4_pass = e4_frame['PASS TD']
e5_pass = e5_frame['PASS TD']
plt.title('Average Passing Touchdowns per Team per Game per Epoch')
plt.ylabel('Number of Passing Touchdowns')
plt.xlabel('Epochs')
plt.boxplot ([e1_pass, e2_pass, e3_pass, e4_pass, e5_pass])
plt.xticks([1, 2, 3, 4, 5], ["1940-1955", "1956-1973", "1974-1993", "1994-2015", "2016-2022"])
plt.show()            


e1_rush = e1_frame['RUSH TD']
e2_rush = e2_frame['RUSH TD']
e3_rush = e3_frame['RUSH TD']
e4_rush = e4_frame['RUSH TD']
e5_rush = e5_frame['RUSH TD']
plt.title('Average Rushing Touchdowns per Team per Game per Epoch')
plt.ylabel('Number of Rushing Touchdowns')
plt.xlabel('Epochs')
plt.boxplot ([e1_rush, e2_rush, e3_rush, e4_rush, e5_rush])
plt.xticks([1, 2, 3, 4, 5], ["1940-1955", "1956-1973", "1974-1993", "1994-2015", "2016-2022"])
plt.show()


e1_fg = e1_frame['FGM']
e2_fg = e2_frame['FGM']
e3_fg = e3_frame['FGM']
e4_fg = e4_frame['FGM']
e5_fg = e5_frame['FGM']
plt.title('Average Field Goals per Team per Game per Epoch')
plt.ylabel('Number of Field Goals')
plt.xlabel('Epochs')
plt.boxplot ([e1_fg, e2_fg, e3_fg, e4_fg, e5_fg])
plt.xticks([1, 2, 3, 4, 5], ["1940-1955", "1956-1973", "1974-1993", "1994-2015", "2016-2022"])
plt.show()


e1_xp = e1_frame['XPM']
e2_xp = e2_frame['XPM']
e3_xp = e3_frame['XPM']
e4_xp = e4_frame['XPM']
e5_xp = e5_frame['XPM']
plt.title('Average Extra Points per Team per Game per Epoch')
plt.ylabel('Number of Extra Points')
plt.xlabel('Epochs')
plt.boxplot ([e1_xp, e2_xp, e3_xp, e4_xp, e5_xp])
plt.xticks([1, 2, 3, 4, 5], ["1940-1955", "1956-1973", "1974-1993", "1994-2015", "2016-2022"])
plt.show()

e1_xp2 = e1_frame['XP2']
e2_xp2 = e2_frame['XP2']
e3_xp2 = e3_frame['XP2']
e4_xp2 = e4_frame['XP2']
e5_xp2 = e5_frame['XP2']
plt.title('Average Two Point Conversions per Team per Game per Epoch')
plt.ylabel('Number of Two Point Conversions')
plt.xlabel('Epochs')
plt.boxplot ([e1_xp2, e2_xp2, e3_xp2, e4_xp2, e5_xp2])
plt.xticks([1, 2, 3, 4, 5], ["1940-1955", "1956-1973", "1974-1993", "1994-2015", "2016-2022"])
plt.show()

e1_sfty = e1_frame['SFTY']
e2_sfty = e2_frame['SFTY']
e3_sfty = e3_frame['SFTY']
e4_sfty = e4_frame['SFTY']
e5_sfty = e5_frame['SFTY']
plt.title('Average Safeties per Team per Game per Epoch')
plt.ylabel('Number of Safeties')
plt.xlabel('Epochs')
plt.boxplot ([e1_sfty, e2_sfty, e3_sfty, e4_sfty, e5_sfty])
plt.xticks([1, 2, 3, 4, 5], ["1940-1955", "1956-1973", "1974-1993", "1994-2015", "2016-2022"])
plt.show()


e1_ret = e1_frame['RET TD']
e2_ret = e2_frame['RET TD']
e3_ret = e3_frame['RET TD']
e4_ret = e4_frame['RET TD']
e5_ret = e5_frame['RET TD']
plt.title('Average Return Touchdown per Team per Game per Epoch')
plt.ylabel('Number of Return Touchdowns')
plt.xlabel('Epochs')
plt.boxplot ([e1_ret, e2_ret, e3_ret, e4_ret, e5_ret])
plt.xticks([1, 2, 3, 4, 5], ["1940-1955", "1956-1973", "1974-1993", "1994-2015", "2016-2022"])
plt.show()


# In[109]:


pip install seaborn


# In[112]:


import plotly.express as px

df = pd.read_csv("NFLGameData(RegSeason1940-2023).csv")

td_graph = px.histogram(e1_td, x='TD')

fig.show()


# In[56]:


import matplotlib.patches as mpatches

df = pd.read_csv("NFLGameData(RegSeason1940-2023).csv")

season_list = list(range(1940,2023))

szn_avg_td = {}
szn_avg_pass_td = {}
szn_avg_rush_td = {}
szn_avg_ret_td = {}
szn_avg_fg = {}
szn_avg_xp = {}
szn_avg_xp2 = {}
szn_avg_sfty = {}

for year in season_list:
    szn_avg_td[year] = 0
    szn_avg_pass_td[year] = 0
    szn_avg_rush_td[year] = 0
    szn_avg_ret_td[year] = 0
    szn_avg_fg[year] = 0
    szn_avg_xp[year] = 0
    szn_avg_xp2[year] = 0
    szn_avg_sfty[year] = 0

    
for year in season_list:
    new_df = df[(df['SEASON'] == year)]
    length=len(new_df)
    for index, row in new_df.iterrows():
        szn_avg_td[year] += row['TD']
        szn_avg_pass_td[year] += row['PASS TD']
        szn_avg_rush_td[year] += row['RUSH TD']
        szn_avg_ret_td[year] += row['RET TD']
        szn_avg_fg[year] += row['FGM']
        szn_avg_xp[year] += row['XPM']
        szn_avg_xp2[year] += row['XP2']
        szn_avg_sfty[year] += row['SFTY']
    
    szn_avg_td[year] = szn_avg_td[year]/length
    szn_avg_pass_td[year] = szn_avg_pass_td[year]/length
    szn_avg_rush_td[year] = szn_avg_rush_td[year]/length
    szn_avg_ret_td[year] = szn_avg_ret_td[year]/length
    szn_avg_fg[year] = szn_avg_fg[year]/length
    szn_avg_xp[year] = szn_avg_xp[year]/length
    szn_avg_xp2[year] = szn_avg_xp2[year]/length
    szn_avg_sfty[year] = szn_avg_sfty[year]/length

e1=1940
e2=1955
e3=1973
e4=1993
e5=2015
e6=2022
white_patch = mpatches.Patch(color='white', label='1940-1955')
powderblue_patch = mpatches.Patch(color='powderblue', label='1956-1973')
cyan_patch = mpatches.Patch(color='cyan', label='1974-1993')
deepskyblue_patch = mpatches.Patch(color='deepskyblue', label='1993-2015')
blue_patch = mpatches.Patch(color='blue', label='2016-2022')


plt.ylabel("Num of Touchdowns")
plt.xlabel("Season")
plt.title("Number of Touchdowns per Team per Game per Season (1940-2023)")
plt.plot(szn_avg_td.keys(), szn_avg_td.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
#ax.legend(handles=[white_patch])
plt.show()

plt.ylabel("Num of FG")
plt.xlabel("Season")
plt.title("Number of FG's per Team per Game per Season (1940-2023)")
plt.plot(szn_avg_fg.keys(), szn_avg_fg.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Pass TD")
plt.xlabel("Season")
plt.title("Number of Pass TD per Team per Game per Season (1940-2023)")
plt.plot(szn_avg_pass_td.keys(), szn_avg_pass_td.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Rush TD")
plt.xlabel("Season")
plt.title("Number of Rush TD per Team per Game per Season (1940-2023)")
plt.plot(szn_avg_rush_td.keys(), szn_avg_rush_td.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Extra Points")
plt.xlabel("Season")
plt.title("Number of Extra Points per Team per Game per Season (1940-2023)")
plt.plot(szn_avg_xp.keys(), szn_avg_xp.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Two Point Conversions")
plt.xlabel("Season")
plt.title("Number of Two Point Conversions per Team per Game per Season (1940-2023)")
plt.plot(szn_avg_xp2.keys(), szn_avg_xp2.values(), color='red')
# plt.axvspan(e1, e2, color='white', alpha=0.5)
# plt.axvspan(e2, e3, color='powederblue', alpha=0.5)
#plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Safeties")
plt.xlabel("Season")
plt.title("Number of Safeties per Team per Game per Season (1940-2023)")
plt.plot(szn_avg_sfty.keys(), szn_avg_sfty.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()


# In[64]:


team_list = ['Chicago Bears', 'Cincinnati Bengals'
, 'Cleveland Browns', 'Green Bay Packers', 'Miami Dolphins', 'Washington', 'Denver Broncos', 'Patriots', 'Dallas Cowboys', 'Colts', 'Rams', 'Seahawks', 'Vikings', 'Chargers', 'San Francisco', 'Steelers', 'Eagles', 'Raiders', 'Chiefs', 'Chargers']


team = 'Giants'

driver = webdriver.Chrome()
driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-playoff-game-in-1933")
driver.implicitly_wait(5)
html = driver.page_source
tables = pd.read_html(html)
driver.implicitly_wait(5)
nfl_games = tables[0]
    
# for year in range(1920, 2000):
#     driver = webdriver.Chrome()
#     driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-playoff-game-in-" +str(year))
#     time=random.SystemRandom().uniform(1, 3)
#     driver.implicitly_wait(time)
#     html = driver.page_source
#     driver.implicitly_wait(time)
#     try:
#         tables = pd.read_html(html)
#         nfl_games = pd.concat([nfl_games, tables[0]])
#         #count += 1
#         if (nfl_games.columns.tolist() != tables[0].columns.tolist()):
#             print("Columns do not match.")    
#     except ValueError:
#         continue

# problems = []

for team in team_list:
    
    
    for year in range(1920, 2000):
        
        driver = webdriver.Chrome()
        driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-playoff-game-in-" + str(year) + "nfl")
        time=random.SystemRandom().uniform(1, 3)

        # import random and use random number between 7 and 12
        driver.implicitly_wait(time)

        html = driver.page_source

        # import random and use random number between 7 and 12
        driver.implicitly_wait(time)
    
        try:
            tables = pd.read_html(html)
            nfl_games = pd.concat([nfl_games, tables[0]])
            #count += 1
    
            if (nfl_games.columns.tolist() != tables[0].columns.tolist()):
                print("Columns do not match.")
                problems.append(str(team)+ " "+ str(year))
                
                
        except ValueError:
            continue

        driver.close()
        
nfl_games.to_csv('RESCRAPE_PLAYOFF_TAKE_2.csv')



# In[139]:


# SCRAPE PROBLEM TEAMS

team = 'Seahawks'

driver = webdriver.Chrome()
driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-" + team + "-have-in-each-playoff-game-in-1983-nfl")
driver.implicitly_wait(5)
html = driver.page_source
tables = pd.read_html(html)
driver.implicitly_wait(5)
nfl_games = tables[0]


for year in range(1984, 2023):
    driver = webdriver.Chrome()
    driver.get("https://www.statmuse.com/nfl/ask/how-many-touchdowns-did-the-"+team+"-have-in-each-playoff-game-in-" +str(year)+"-nfl")
    time=random.SystemRandom().uniform(1, 3)
    driver.implicitly_wait(time)
    html = driver.page_source
    driver.implicitly_wait(time)
    try:
        tables = pd.read_html(html)
        nfl_games = pd.concat([nfl_games, tables[0]])
        #count += 1
        if (nfl_games.columns.tolist() != tables[0].columns.tolist()):
            print("Columns do not match.")    
    except ValueError:
        continue

print(nfl_games)
nfl_games.to_csv('SeahawksPlayoffs.csv')


# In[107]:


df = pd.read_csv("EveryScorigami.csv")

e0=1920
e1=1940
e2=1955
e3=1973
e4=1993
e5=2015
e6=2022

scorigami_dict = {}
season_list = []

for year in range(1920, 2023):
    scorigami_dict[year]=0

for index, row in df.iterrows():
    if row['New Scorigami?']:
        scorigami_dict[row['Season']]+=1

plt.ylabel("Scorigamis")
plt.xlabel("Seasons")
plt.title("Number of New Scorigamis per Season (1920-2023)")
plt.plot(scorigami_dict.keys(), scorigami_dict.values(), color='red')
plt.axvspan(e0, e1, color='white', alpha=0.5)
plt.axvspan(e1, e2, color='gainsboro', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()


# In[116]:


# ADD EPOCH COLUMN

df = pd.read_csv("NFLGameData(RegSeason1940-2023).csv")

epoch_list = []

for index, row in df.iterrows():
    if (row['SEASON'] >=1940 and row['SEASON'] <=1955):
        epoch_list.append('1940-1955')
    elif (row['SEASON'] >=1956 and row['SEASON'] <=1973):
        epoch_list.append('1956-1973')
    elif (row['SEASON'] >=1974 and row['SEASON'] <=1993):
        epoch_list.append('1974-1993')
    elif (row['SEASON'] >=1994 and row['SEASON'] <=2015):
        epoch_list.append('1994-2015')
    elif (row['SEASON'] >=2016 and row['SEASON'] <=2022):
        epoch_list.append('2016-2022')    

df['EPOCH'] = epoch_list

df.to_csv('EpochCheck.csv')


# In[121]:


import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = pd.read_csv("NFLGameData(RegSeason1940-2023).csv")
g = sb.FacetGrid(df, col = "EPOCH")
g.map(plt.hist, "TD")
plt.show()

g = sb.FacetGrid(df, col = "EPOCH")
g.map(plt.hist, "RUSH TD")
plt.show()


g = sb.FacetGrid(df, col = "EPOCH")
g.map(plt.hist, "PASS TD")
plt.show()


g = sb.FacetGrid(df, col = "EPOCH")
g.map(plt.hist, "RET TD")
plt.show()


g = sb.FacetGrid(df, col = "EPOCH")
g.map(plt.hist, "FGM")
plt.show()


g = sb.FacetGrid(df, col = "EPOCH")
g.map(plt.hist, "XPM")
plt.show()


g = sb.FacetGrid(df, col = "EPOCH")
g.map(plt.hist, "XP2")
plt.show()


g = sb.FacetGrid(df, col = "EPOCH")
g.map(plt.hist, "SFTY")
plt.show()


# In[142]:


import matplotlib.patches as mpatches

df = pd.read_csv("NFLGameData(Playoffs).csv")

season_list = list(range(1940,2023))

playoff_avg_td = {}
playoff_avg_pass_td = {}
playoff_avg_rush_td = {}
playoff_avg_ret_td = {}
playoff_avg_fg = {}
playoff_avg_xp = {}
playoff_avg_xp2 = {}
playoff_avg_sfty = {}

for year in season_list:
    playoff_avg_td[year] = 0
    playoff_avg_pass_td[year] = 0
    playoff_avg_rush_td[year] = 0
    playoff_avg_ret_td[year] = 0
    playoff_avg_fg[year] = 0
    playoff_avg_xp[year] = 0
    playoff_avg_xp2[year] = 0
    playoff_avg_sfty[year] = 0

    
for year in season_list:
    new_df = df[(df['SEASONS'] == year)]
    length=len(new_df)
    for index, row in new_df.iterrows():
        playoff_avg_td[year] += row['TD']
        playoff_avg_pass_td[year] += row['PASS TD']
        playoff_avg_rush_td[year] += row['RUSH TD']
        playoff_avg_ret_td[year] += row['RET TD']
        playoff_avg_fg[year] += row['FGM']
        playoff_avg_xp[year] += row['XPM']
        playoff_avg_xp2[year] += row['XP2']
        playoff_avg_sfty[year] += row['SFTY']
    
    playoff_avg_td[year] = playoff_avg_td[year]/length
    playoff_avg_pass_td[year] = playoff_avg_pass_td[year]/length
    playoff_avg_rush_td[year] = playoff_avg_rush_td[year]/length
    playoff_avg_ret_td[year] = playoff_avg_ret_td[year]/length
    playoff_avg_fg[year] = playoff_avg_fg[year]/length
    playoff_avg_xp[year] = playoff_avg_xp[year]/length
    playoff_avg_xp2[year] = playoff_avg_xp2[year]/length
    playoff_avg_sfty[year] = playoff_avg_sfty[year]/length

e1=1940
e2=1955
e3=1973
e4=1993
e5=2015
e6=2022
white_patch = mpatches.Patch(color='white', label='1940-1955')
powderblue_patch = mpatches.Patch(color='powderblue', label='1956-1973')
cyan_patch = mpatches.Patch(color='cyan', label='1974-1993')
deepskyblue_patch = mpatches.Patch(color='deepskyblue', label='1993-2015')
blue_patch = mpatches.Patch(color='blue', label='2016-2022')


plt.ylabel("Num of Touchdowns")
plt.xlabel("Season")
plt.title("Number of Touchdowns per Team per Game per Season (1940-2023)")
plt.plot(playoff_avg_td.keys(), playoff_avg_td.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
#ax.legend(handles=[white_patch])
plt.show()

plt.ylabel("Num of FG")
plt.xlabel("Season")
plt.title("Number of FG's per Team per Game per Season (1940-2023)")
plt.plot(playoff_avg_fg.keys(), playoff_avg_fg.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Pass TD")
plt.xlabel("Season")
plt.title("Number of Pass TD per Team per Game per Season (1940-2023)")
plt.plot(playoff_avg_pass_td.keys(), playoff_avg_pass_td.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Rush TD")
plt.xlabel("Season")
plt.title("Number of Rush TD per Team per Game per Season (1940-2023)")
plt.plot(playoff_avg_rush_td.keys(), playoff_avg_rush_td.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Extra Points")
plt.xlabel("Season")
plt.title("Number of Extra Points per Team per Game per Season (1940-2023)")
plt.plot(playoff_avg_xp.keys(), playoff_avg_xp.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Two Point Conversions")
plt.xlabel("Season")
plt.title("Number of Two Point Conversions per Team per Game per Season (1940-2023)")
plt.plot(playoff_avg_xp2.keys(), playoff_avg_xp2.values(), color='red')
# plt.axvspan(e1, e2, color='white', alpha=0.5)
# plt.axvspan(e2, e3, color='powederblue', alpha=0.5)
#plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()

plt.ylabel("Num of Safeties")
plt.xlabel("Season")
plt.title("Number of Safeties per Team per Game per Season (1940-2023)")
plt.plot(playoff_avg_sfty.keys(), playoff_avg_sfty.values(), color='red')
plt.axvspan(e1, e2, color='white', alpha=0.5)
plt.axvspan(e2, e3, color='powderblue', alpha=0.5)
plt.axvspan(e3, e4, color='cyan', alpha=0.5)
plt.axvspan(e4, e5, color='deepskyblue', alpha=0.5)
plt.axvspan(e5, e6, color='blue', alpha=0.5)
plt.show()


# In[ ]:




