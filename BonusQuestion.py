#-- GEO1001.2020--hw01
#-- [Konstantinos Pantelios] 
#-- [5374367]

import numpy as np
import statistics as stat
from matplotlib import pyplot as plt
import scipy
from scipy import stats
import pandas as pd
import seaborn as sns


#### The next two line are used ONLY to help implement the fucntion "statistics" to ####
# compute and print the mean, variance and st_deviation of the each variable of the 5 sensors.
locations = ["hw01/HEAT - A_final.xls","hw01/HEAT - B_final.xls","hw01/HEAT - C_final.xls","hw01/HEAT - D_final.xls","hw01/HEAT - E_final.xls"]
no_rows = [0,1,2,3]
########################################################################################

######## The next 5 lines create the MAIN dataframes for each of the 5 sensors. ########
df_a=pd.read_excel("hw01/HEAT - A_final.xls",nrows=None,header =3)
df_b=pd.read_excel("hw01/HEAT - B_final.xls",nrows=None,header =3)
df_c=pd.read_excel("hw01/HEAT - C_final.xls",nrows=None,header =3)
df_d=pd.read_excel("hw01/HEAT - D_final.xls",nrows=None,header =3)
df_e=pd.read_excel("hw01/HEAT - E_final.xls",nrows=None,header =3)

#### The next 5 line manipulate the dataframes to make them easier to ues later. #######
df_a = df_a.drop([0]).reset_index(drop=True)
df_b = df_b.drop([0]).reset_index(drop=True)
df_c = df_c.drop([0]).reset_index(drop=True)
df_d = df_d.drop([0]).reset_index(drop=True)
df_e = df_e.drop([0]).reset_index(drop=True)
#########################################################################################

######## The code below creates new smaller dataframes for      #########################
# each of the 5 sensors for the                                 #########################
# variables: Temperature, Wind Speed and Wind Direction (True). #########################

#Temperature
temp_a=df_a["Temperature"]
temp_b=df_b["Temperature"]
temp_c=df_c["Temperature"]
temp_d=df_d["Temperature"]
temp_e=df_e["Temperature"]

# The below 2 line are used ONYL in the implementation of PMF
frames_temp=[temp_a,temp_b,temp_c,temp_d,temp_e] 
temp_AE = pd.concat(frames_temp).dropna().reset_index(drop=True).astype(float)

#Wind Speed
ws_a=df_a["Wind Speed"]
ws_b=df_b["Wind Speed"]
ws_c=df_c["Wind Speed"]
ws_d=df_d["Wind Speed"]
ws_e=df_e["Wind Speed"]
# The below 2 line are used ONYL in the implementation of PDF (consquentaly on KDE)
frames_ws=[ws_a,ws_b,ws_c,ws_d,ws_e]
ws_AE = pd.concat(frames_ws).dropna().reset_index(drop=True).astype(float)

#Wind Direction
wd_a=df_a["Direction ‚ True"]
wd_b=df_b["Direction ‚ True"]
wd_c=df_c["Direction ‚ True"]
wd_d=df_d["Direction ‚ True"]
wd_e=df_e["Direction ‚ True"]


cws_a=df_a["Crosswind Speed"]
cws_b=df_b["Crosswind Speed"]
cws_c=df_c["Crosswind Speed"]
cws_d=df_d["Crosswind Speed"]
cws_e=df_e["Crosswind Speed"]

wbg_a=df_a["WBGT"]
wbg_b=df_b["WBGT"]
wbg_c=df_c["WBGT"]
wbg_d=df_d["WBGT"]
wbg_e=df_e["WBGT"]


######## FOR 1. AFTER LESSON A1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


##### 1st Bullet Point-> Compute mean statistics (mean, variance and standard deviation for each of the sensors variables), ########################################
# what do you observe from the results?



######## FOR 2. AFTER LESSON A2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#### Plot PMF, PDF and CDF for the 5 sensors Temperature values.
#Describe the behaviour of the distributions, are they all similar?
#what about their tails?

## Solution for 1st bullet point of 2 ##

lista=["Direction ‚ True", "Wind Speed", "Crosswind Speed", "Headwind Speed",
 "Temperature", "Globe Temperature","Wind Chill","Relative Humidity","Heat Stress Index",
 "Dew Point","Psychro Wet Bulb Temperature","Station Pressure","Barometric Pressure",
 "Altitude", "Density Altitude", "NA Wet Bulb Temperature", "WBGT", "TWL", "Direction ‚ Mag"]

lista1=['A-B','A-C','A-D','A-E','B-C','B-D','B-E','C-D','C-E','D-E']
###### NEW COOODE ######## CORRELATION
##### NEWWWWW CODEEE KERNEL######
from datetime import datetime, timedelta



ttemp_a=df_a[["FORMATTED DATE-TIME","Temperature"]]
ttemp_b=df_b[["FORMATTED DATE-TIME","Temperature"]]
ttemp_c=df_c[["FORMATTED DATE-TIME","Temperature"]]
ttemp_d=df_d[["FORMATTED DATE-TIME","Temperature"]]
ttemp_e=df_e[["FORMATTED DATE-TIME","Temperature"]]
sensor_df=[ttemp_a,ttemp_b,ttemp_c,ttemp_d,ttemp_e]


def data(x):
    df=pd.DataFrame()
    date="2020-06-10"

    for i in range(35):
    
        a=x[x["FORMATTED DATE-TIME"].astype(str).str.contains(date)]
        b=a["Temperature"].astype(float)
        df=df.append({"Days":date , "Temperature" : b.mean()},ignore_index=True)
        df2=df.append({"Days":date , "Temperature" : b.min()},ignore_index=True)

        date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    return df,df2
   

ttemp_a=data(ttemp_a)[0]
ttemp_a=ttemp_a.rename(columns={"Temperature":"Temperature_A"}, inplace=False)
ttemp_b=data(ttemp_b)[0]
ttemp_b=ttemp_b.rename(columns={"Temperature":"Temperature_B"}, inplace=False)
ttemp_c=data(ttemp_c)[0]
ttemp_c=ttemp_c.rename(columns={"Temperature":"Temperature_C"}, inplace=False)
ttemp_d=data(ttemp_d)[0]
ttemp_d=ttemp_d.rename(columns={"Temperature":"Temperature_D"}, inplace=False)
ttemp_e=data(ttemp_e)[0]
ttemp_e=ttemp_e.rename(columns={"Temperature":"Temperature_E"}, inplace=False)


j_a=ttemp_a["Temperature_A"]
j_b=ttemp_b["Temperature_B"]
j_c=ttemp_c["Temperature_C"]
j_d=ttemp_d["Temperature_D"]
j_e=ttemp_e["Temperature_E"]

all_df=ttemp_a
all_df=all_df.join(j_b)
all_df=all_df.join(j_c)
all_df=all_df.join(j_d)
all_df=all_df.join(j_e)


all_df.plot.bar(x="Days",y=["Temperature_A","Temperature_B","Temperature_C","Temperature_D","Temperature_E"],subplots=True)
plt.get_current_fig_manager().window.state('zoomed')
#plt.show()



print("Max. Temperature in day:"+"\n",round(ttemp_a[ttemp_a["Temperature_A"]==all_df["Temperature_A"].max()].reset_index(drop=True),2))
print("Min. Temperature in day:"+"\n",round(ttemp_a[ttemp_a["Temperature_A"]==all_df["Temperature_A"].min()].reset_index(drop=True),2))
print("Max. Temperature in day:"+"\n",round(ttemp_b[ttemp_b["Temperature_B"]==all_df["Temperature_B"].max()].reset_index(drop=True),2))
print("Min. Temperature in day:"+"\n",round(ttemp_b[ttemp_b["Temperature_B"]==all_df["Temperature_B"].min()].reset_index(drop=True),2))
print("Max. Temperature in day:"+"\n",round(ttemp_c[ttemp_c["Temperature_C"]==all_df["Temperature_C"].max()].reset_index(drop=True),2))
print("Min. Temperature in day:"+"\n",round(ttemp_c[ttemp_c["Temperature_C"]==all_df["Temperature_C"].min()].reset_index(drop=True),2))
print("Max. Temperature in day:"+"\n",round(ttemp_d[ttemp_d["Temperature_D"]==all_df["Temperature_D"].max()].reset_index(drop=True),2))
print("Min. Temperature in day:"+"\n",round(ttemp_d[ttemp_d["Temperature_D"]==all_df["Temperature_D"].min()].reset_index(drop=True),2))
print("Max. Temperature in day:"+"\n",round(ttemp_e[ttemp_e["Temperature_E"]==all_df["Temperature_E"].max()].reset_index(drop=True),2))
print("Min. Temperature in day:"+"\n",round(ttemp_e[ttemp_e["Temperature_E"]==all_df["Temperature_E"].min()].reset_index(drop=True),2))