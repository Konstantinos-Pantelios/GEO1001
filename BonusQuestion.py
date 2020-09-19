#-- GEO1001.2020--hw01
#-- [Konstantinos Pantelios] 
#-- [5374367]
#-------------------------------- The code is for bonus question ---------------------------------
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


from datetime import datetime, timedelta


# Creates usefull dataframe
ttemp_a=df_a[["FORMATTED DATE-TIME","Temperature"]]
ttemp_b=df_b[["FORMATTED DATE-TIME","Temperature"]]
ttemp_c=df_c[["FORMATTED DATE-TIME","Temperature"]]
ttemp_d=df_d[["FORMATTED DATE-TIME","Temperature"]]
ttemp_e=df_e[["FORMATTED DATE-TIME","Temperature"]]
sensor_df=[ttemp_a,ttemp_b,ttemp_c,ttemp_d,ttemp_e]


def data(x):
    """the function groups the measurments of the Temperature by day (for all sensorns), The variable x is the dataframe of Temperature"""

    df=pd.DataFrame()
    date="2020-06-10"

    for i in range(35):
    
        a=x[x["FORMATTED DATE-TIME"].astype(str).str.contains(date)]
        b=a["Temperature"].astype(float)
        df=df.append({"Days":date , "Temperature" : b.mean()},ignore_index=True)

        date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    return df
   

ttemp_a=data(ttemp_a)
ttemp_a=ttemp_a.rename(columns={"Temperature":"Temperature_A"}, inplace=False)
ttemp_b=data(ttemp_b)
ttemp_b=ttemp_b.rename(columns={"Temperature":"Temperature_B"}, inplace=False)
ttemp_c=data(ttemp_c)
ttemp_c=ttemp_c.rename(columns={"Temperature":"Temperature_C"}, inplace=False)
ttemp_d=data(ttemp_d)
ttemp_d=ttemp_d.rename(columns={"Temperature":"Temperature_D"}, inplace=False)
ttemp_e=data(ttemp_e)
ttemp_e=ttemp_e.rename(columns={"Temperature":"Temperature_E"}, inplace=False)

# Creates the all_df dataframe which contains all the Temperature means of the sensors by day.
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
plt.show() #Activate line to plot the figure



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