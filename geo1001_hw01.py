#-- GEO1001.2020--hw01
#-- [Konstantinos Pantelios] 
#-- [5374367]

####
# Importing libraries that are being used in the code
import numpy as np
import statistics as stat
from matplotlib import pyplot as plt
from scipy import stats
import pandas as pd
import seaborn as sns


#### The next eight line are used ONLY to help implement the fucntion "statistics" to ####
# compute and print the mean, variance and st_deviation of the each variable of the 5 sensors.
locations = ["hw01/HEAT - A_final.xls","hw01/HEAT - B_final.xls",
"hw01/HEAT - C_final.xls","hw01/HEAT - D_final.xls",
"hw01/HEAT - E_final.xls"]
no_rows = [0,1,2,3]
lista=["Direction ‚ True", "Wind Speed", "Crosswind Speed", "Headwind Speed",
 "Temperature", "Globe Temperature","Wind Chill","Relative Humidity","Heat Stress Index",
 "Dew Point","Psychro Wet Bulb Temperature","Station Pressure","Barometric Pressure",
 "Altitude", "Density Altitude", "NA Wet Bulb Temperature", "WBGT", "TWL", "Direction ‚ Mag"]
sensors=["A","B","C","D","E"]
#### The line below is used ONLY for the correlation functions in the code (lines: 548, 551)
lista1=['A-B','A-C','A-D','A-E','B-C','B-D','B-E','C-D','C-E','D-E']
########################################################################################

######## The next 5 lines create the MAIN dataframes for each of the 5 sensors. ########
df_a=pd.read_excel("hw01/HEAT - A_final.xls",nrows=None,header =3)
df_b=pd.read_excel("hw01/HEAT - B_final.xls",nrows=None,header =3)
df_c=pd.read_excel("hw01/HEAT - C_final.xls",nrows=None,header =3)
df_d=pd.read_excel("hw01/HEAT - D_final.xls",nrows=None,header =3)
df_e=pd.read_excel("hw01/HEAT - E_final.xls",nrows=None,header =3)

#### The next 5 lines manipulate the dataframes to make them easier to use later. #######
df_a = df_a.drop([0]).reset_index(drop=True)
df_b = df_b.drop([0]).reset_index(drop=True)
df_c = df_c.drop([0]).reset_index(drop=True)
df_d = df_d.drop([0]).reset_index(drop=True)
df_e = df_e.drop([0]).reset_index(drop=True)
#########################################################################################

######## The code below creates new smaller dataframes for      #########################
# each of the 5 sensors for the                                 #########################
# variables: Temperature, Wind Speed, Wind Direction (True)     #########################
# and Wet Bulb Globe Temperature.                               #########################

#Temperature
temp_a=df_a["Temperature"]
temp_b=df_b["Temperature"]
temp_c=df_c["Temperature"]
temp_d=df_d["Temperature"]
temp_e=df_e["Temperature"]

#Wind Speed
ws_a=df_a["Wind Speed"]
ws_b=df_b["Wind Speed"]
ws_c=df_c["Wind Speed"]
ws_d=df_d["Wind Speed"]
ws_e=df_e["Wind Speed"]

#Wind Direction
wd_a=df_a["Direction ‚ True"]
wd_b=df_b["Direction ‚ True"]
wd_c=df_c["Direction ‚ True"]
wd_d=df_d["Direction ‚ True"]
wd_e=df_e["Direction ‚ True"]

#Cross Wind Speed
cws_a=df_a["Crosswind Speed"]
cws_b=df_b["Crosswind Speed"]
cws_c=df_c["Crosswind Speed"]
cws_d=df_d["Crosswind Speed"]
cws_e=df_e["Crosswind Speed"]

#Wet Bulb Globe Temperature 
wbg_a=df_a["WBGT"]
wbg_b=df_b["WBGT"]
wbg_c=df_c["WBGT"]
wbg_d=df_d["WBGT"]
wbg_e=df_e["WBGT"]


######## FOR 1. AFTER LESSON A1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


##### 1st Bullet Point of 1-> Compute mean statistics (mean, variance and standard deviation for each of the sensors variables), ########################################
# what do you observe from the results?

def statistics(loc,col):
    """Computation of statistical rates: Mean, Variance and Standard deviation"""
    
    a = pd.read_excel(loc, skiprows = no_rows, usecols= col )
    return str(a.values.mean()),str(a.values.var()),str(a.values.std())

## The solution to first bullet point of 1 ##
# Prints the statistical indicators for all of the varibales of the 5 sensors.
for i in range(5):
    dir_t = statistics(locations[i],[1])
    wind_s = statistics(locations[i],[2])
    c_wind_s = statistics(locations[i],[3])
    h_wind_s = statistics(locations[i],[4])
    temp = statistics(locations[i],[5])
    gl_temp = statistics(locations[i],[6])
    wind_ch = statistics(locations[i],[7])
    rel_humid = statistics(locations[i],[8])
    heat_str = statistics(locations[i],[9])
    dew_p = statistics(locations[i],[10])
    psy_wet = statistics(locations[i],[11])
    stat_press = statistics(locations[i],[12])
    barom_press = statistics(locations[i],[13])
    alt = statistics(locations[i],[14])
    dens_alt =statistics(locations[i],[15])
    na_wet = statistics(locations[i],[16])
    wbgt = statistics(locations[i],[17])
    twl = statistics(locations[i],[18])
    dir_mag = statistics(locations[i],[19])
    print("\n","=== VALUES FOR SENSOR:",sensors[i],"=================================================="*2,"\n"+
    "True Direction-> \t mean:",dir_t[0],"\t","variance:",dir_t[1],"\t","standard deviation:",dir_t[2],"\n"
    +"Wind Speed-> \t\t mean:",wind_s[0],"\t","variance:",wind_s[1],"\t","standard deviation:",wind_s[2],"\n"
    +"Crosswind Speed-> \t mean:",c_wind_s[0],"\t","variance:",c_wind_s[1],"\t","standard deviation:",c_wind_s[2],"\n"
    +"Headwind Speed-> \t mean:",h_wind_s[0],"\t","variance:",h_wind_s[1],"\t","standard deviation:",h_wind_s[2],"\n"
    +"Temperature-> \t\t mean:",temp[0],"\t","variance:",temp[1],"\t","standard deviation:",temp[2],"\n"
    +"Globe Temperature-> \t mean:",gl_temp[0],"\t","variance:",gl_temp[1],"\t","standard deviation:",gl_temp[2],"\n"
    +"Wind chill-> \t\t mean:",wind_ch[0],"\t","variance:",wind_ch[1],"\t","standard deviation:",wind_ch[2],"\n"
    +"Relative humidity-> \t mean:",rel_humid[0],"\t","variance:",rel_humid[1],"\t","standard deviation:",rel_humid[2],"\n"
    +"Heat stress index-> \t mean:",heat_str[0],"\t","variance:",heat_str[1],"\t","standard deviation:",heat_str[2],"\n"
    +"Dew point-> \t\t mean:",dew_p[0],"\t","variance:",dew_p[1],"\t","standard deviation:",dew_p[2],"\n"
    +"Psychro Wet Bulb Temp->  mean:",psy_wet[0],"\t","variance:",psy_wet[1],"\t","standard deviation:",psy_wet[2],"\n"
    +"Station pressure-> \t mean:",stat_press[0],"\t","variance:",stat_press[1],"\t","standard deviation:",stat_press[2],"\n"
    +"Barometric pressure-> \t mean:",barom_press[0],"\t","variance:",barom_press[1],"\t","standard deviation:",barom_press[2],"\n"
    +"Altitude-> \t\t mean:",alt[0],"\t","variance:",alt[1],"\t","standard deviation:",alt[2],"\n"
    +"Density Altitude-> \t mean:",dens_alt[0],"\t","variance:",dens_alt[1],"\t","standard deviation:",dens_alt[2],"\n"
    +"NA Wet Bulb Temperature->mean:",na_wet[0],"\t","variance:",na_wet[1],"\t","standard deviation:",na_wet[2],"\n"
    +"WBGT-> \t\t\t mean:",wbgt[0],"\t","variance:",wbgt[1],"\t","standard deviation:",wbgt[2],"\n"
    +"TWL-> \t\t\t mean:",twl[0],"\t","variance:",twl[1],"\t","standard deviation:",twl[2],"\n"
    +"Direction ‚ Mag-> \t mean:",dir_mag[0],"\t","variance:",dir_mag[1],"\t","standard deviation:",dir_mag[2])
#################################################################################################################################################################

##### 2nd Bullet Point of 1-> Create 1 plot that contains histograms for the 5 sensors Temperature values. ##########################################################
# Compare histograms with 5 and 50 bins,  why is the number of bins important?

def hist_temp(a,b,c,d,e,b1,b2): 
    """Creates the 2 Temperature histograms of different bin numers for all of the sensors.
    The variables a,b,c,d,e need to be the dataframes of the temperature of the 5 sensors.
    b1 and b2 correspond to the number of bin that the histogram will generate for comparison."""

    #Sets the figure and title
    fig_1  = plt.figure(1,figsize=(10,10))
    fig_1.canvas.set_window_title('Bin comparison of 5 sensor Temperature Histogram')

    #Sets the position of the 10 plots
    bin5_a=fig_1.add_subplot(521)
    bin50_a=fig_1.add_subplot(522)
    bin5_b=fig_1.add_subplot(523)
    bin50_b=fig_1.add_subplot(524)
    bin5_c=fig_1.add_subplot(525)
    bin50_c=fig_1.add_subplot(526)
    bin5_d=fig_1.add_subplot(527)
    bin50_d=fig_1.add_subplot(528)
    bin5_e=fig_1.add_subplot(529)
    bin50_e=fig_1.add_subplot(5,2,10)

    #Creates the histogramms and sets titles and grid for all of the plots
    bin5_a.hist(x=a,bins=b1, color = 'b')
    bin50_a.hist(x=a,bins=b2, color = 'b')
    bin5_b.hist(x=b,bins=b1, color = 'b')
    bin50_b.hist(x=b,bins=b2, color = 'b')
    bin5_c.hist(x=c,bins=b1, color = 'b')
    bin50_c.hist(x=c,bins=b2, color = 'b')
    bin5_d.hist(x=d,bins=b1, color = 'b')
    bin50_d.hist(x=d,bins=b2, color = 'b')
    bin5_e.hist(x=e,bins=b1, color = 'b')
    bin50_e.hist(x=e,bins=b2, color = 'b')
    bin5_a.set_title("Sens_A: Temperature Histogram of 5 bins")
    bin50_a.set_title("Sens_A: Temperature Histogram of 50 bins")
    bin5_a.grid(axis="both")
    bin50_a.grid(axis="both")
    bin5_b.set_title("Sens_B: Temperature Histogram of 5 bins")
    bin50_b.set_title("Sens_B: Temperature Histogram of 50 bins")
    bin5_b.grid(axis="both")
    bin50_b.grid(axis="both")
    bin5_c.set_title("Sens_C: Temperature Histogram of 5 bins")
    bin50_c.set_title("Sens_C: Temperature Histogram of 50 bins")
    bin5_c.grid(axis="both")
    bin50_c.grid(axis="both")
    bin5_d.set_title("Sens_D: Temperature Histogram of 5 bins")
    bin50_d.set_title("Sens_D: Temperature Histogram of 50 bins")
    bin5_d.grid(axis="both")
    bin50_d.grid(axis="both")
    bin5_e.set_title("Sens_E: Temperature Histogram of 5 bins")
    bin50_e.set_title("Sens_E: Temperature Histogram of 50 bins")
    bin5_e.grid(axis="both")
    bin50_e.grid(axis="both")

    plt.get_current_fig_manager().window.state('zoomed')
    fig_1.tight_layout()
    plt.show()  

## the solution to the 2nd bullet point of 1 ##
#Calling the function "hist_temp".The input in the function is the temperature dataframes for the 5 sensors
# converted from object to float and the number of the bins to compare.
hist_temp(temp_a.astype(float),temp_b.astype(float),temp_c.astype(float),temp_d.astype(float),temp_e.astype(float),5,50) 
##########################################################################################################################################################

#### 3rd Bullet Point of 1 -> Create 1 plot where frequency poligons for the 5 sensors ###################################################################
#Temperature values overlap in different colors with a legend. 
 
def hist_temp_sens(a,b,c,d,e):
    """Generates an overlapping plot of friquency polygons for the Temperature of 5 sensors.
    The variables a,b,c,d,e should be the Temperature dataframes of the respective sensors."""
    
    #Sets the figure and title
    fig_10 = plt.figure()
    fig_10.canvas.set_window_title('Frequency polygons of Temperature')

    #Sets the position of the 5 plots which basically the same position (ovelap)
    ax_a = fig_10.add_subplot(111)
    ax_b = fig_10.add_subplot(111)
    ax_c = fig_10.add_subplot(111)
    ax_d = fig_10.add_subplot(111)
    ax_e = fig_10.add_subplot(111)

    #Sets the histogram's values and the bins range (for the 5 sensors)
    [fr_a,bins]=np.histogram(a,bins=50)
    [fr_b,bins]=np.histogram(b,bins=50)
    [fr_c,bins]=np.histogram(c,bins=50)
    [fr_d,bins]=np.histogram(d,bins=50)
    [fr_e,bins]=np.histogram(e,bins=50)

    #Set the cumulative sum of the above histogram values into new variables (for the 5 sensors)
    cdf_A = np.cumsum(fr_a)
    cdf_B = np.cumsum(fr_b)
    cdf_C = np.cumsum(fr_c)
    cdf_D = np.cumsum(fr_d)
    cdf_E = np.cumsum(fr_e)

    #x = np.linspace(0,10,1000)
    #Ploting the 5 axis using the above arrays and the bin range.
    ax_a.plot(bins[:-1],cdf_A,label= "Sensor A")
    ax_b.plot(bins[:-1],cdf_B,label= "Sensor B")
    ax_c.plot(bins[:-1],cdf_C,label= "Sensor C")
    ax_d.plot(bins[:-1],cdf_D,label= "Sensor D")
    ax_e.plot(bins[:-1],cdf_E,label= "Sensor E")
   
   #Adding title, grid, legend and axis labels to the graph
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Temperature', fontsize=9)
    plt.ylabel('Cumulative number of samples', fontsize=9)
    plt.title("Frequency polygons of the 5 sensors for Temperature")
    plt.legend(loc= "lower right", title = "Legend")
    plt.tick_params(labelsize=9)
    
    plt.get_current_fig_manager().window.state('zoomed')
    fig_10.tight_layout()
    plt.show()

## the solution to the 3rd Bullet point of 1 ##
#Calling the function "hist_temp_sens" to generate the frequency polygons graph.
# The input in the function is the temperature dataframes for the 5 sensors converted from object to float.
hist_temp_sens(temp_a.astype(float),temp_b.astype(float),temp_c.astype(float),temp_d.astype(float),temp_e.astype(float))
#################################################################################################################################################################

#### 4th Bullet Point of 1 -> Generate 3 plots that include the 5 sensors boxplot for: ##########################################################################
#  Wind Speed, Wind Direction and Temperature.

def boxplt(t_a,t_b,t_c,t_d,t_e,s_a,s_b,s_c,s_d,s_e,d_a,d_b,d_c,d_d,d_e): 
    """ Generates three (3) boxplots each for the variables "Temperature", "Wind Speed" and "Wind Direction , True"
    for the 5 different sensors.
    The variables t_a,t_b,t_c,t_d,t_e,s_a,s_b,s_c,s_d,s_e,d_a,d_b,d_c,d_d,d_e take as input the corrisponding dataframes of the
    5 sensors for the "Temperature":[t_a,t_b,t_c,t_d,t_e], "Wind Speed":[s_a,s_b,s_c,s_d,s_e], "Wind Direction , True":[d_a,d_b,d_c,d_d,d_e]."""

    #Sets the inputs (dataframes) into different lists for easier use in boxplot method. 
    data_t=[t_a,t_b,t_c,t_d,t_e]
    data_s=[s_a,s_b,s_c,s_d,s_e]
    data_d=[d_a,d_b,d_c,d_d,d_e]

    #Sets the figure and axes with fixed postitions + title
    fig_3, axes = plt.subplots(1,3)
    fig_3.canvas.set_window_title('Boxplots of the 5 sensors for Temerature, Wind Speed and Wind Direction')

    #Generates the boxplots, aligns them to thei positions and sets their axis labels.
    axes[2].boxplot(data_t,showmeans=True)
    axes[2].set_ylabel('Temperature')
    axes[2].set_xlabel("Sensors")

    axes[0].boxplot(data_s,showmeans=True)
    axes[0].set_ylabel('Wind Speed')
    axes[0].set_xlabel("Sensors")

    axes[1].boxplot(data_d,showmeans=True)
    axes[1].set_ylabel('Wind Direction (True)')
    axes[1].set_xlabel("Sensors")

    plt.suptitle("Boxplots of the 5 sensors for Wind Speed Wind Direction and Temerature")  
    plt.get_current_fig_manager().window.state('zoomed')
    #fig_3.tight_layout()
    plt.show()

## The solution to the 4th Bullet Point of 1 ##
# Calling the function "boxplt" and setting as input the dataframes for each sensor for the 3 variables
#"Temperature", "Wind Speed" and "Wind Direction , True".
boxplt(temp_a.astype(float),temp_b.astype(float),temp_c.astype(float),temp_d.astype(float),temp_e.astype(float), 
ws_a.astype(float),ws_b.astype(float),ws_c.astype(float),ws_d.astype(float),ws_e.astype(float),
wd_a.astype(float),wd_b.astype(float),wd_c.astype(float),wd_d.astype(float),wd_e.astype(float))
################################################################################################################################################################



######## FOR 2. AFTER LESSON A2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#### 1st Bullet Point of 2 -> Plot PMF, PDF and CDF for the 5 sensors Temperature values.
#Describe the behaviour of the distributions, are they all similar?
#what about their tails?

### Probability Mass Function ###
def pmf_2(sample_r):
    """ Used by the function pmf for its calculation.
    The input sample_r is the dataframe for the temperature."""

    c = sample_r.value_counts()
    p = c/len(sample_r)
    df=p
    c = df.sort_index()
    return c

def pmf(a,b,c,d,e):
    """Creates the PMF for the 5 sensors Temperature values.
    The variables a,b,c,d,e must be the dataframes of the sensors for the Temperature."""

    #Sets the figure
    fig_4= plt.figure(4)
    fig_4.canvas.set_window_title('PMF of the 5 sensor - Temperature Histogram')

    #Set axes in different subplot positions
    t_a=fig_4.add_subplot(231)
    t_b=fig_4.add_subplot(232)
    t_c=fig_4.add_subplot(233)
    t_d=fig_4.add_subplot(223)
    t_e=fig_4.add_subplot(224)
    
    #Calls pmf_2 to get PMF values and Plots Bar graph of the PMF + title
    t_a.bar(pmf_2(a).index,pmf_2(a),width=0.1)
    t_a.set_title("Sens_A: PMF of temperature")
    t_b.bar(pmf_2(b).index,pmf_2(b),width=0.1)
    t_b.set_title("Sens_B: PMF of temperature")
    t_c.bar(pmf_2(c).index,pmf_2(c),width=0.1)
    t_c.set_title("Sens_C: PMF of temperature")
    t_d.bar(pmf_2(d).index,pmf_2(d),width=0.1)
    t_d.set_title("Sens_D: PMF of temperature")
    t_e.bar(pmf_2(e).index,pmf_2(e),width=0.1)
    t_e.set_title("Sens_E: PMF of temperature")   
    
    plt.suptitle('PMF of the 5 sensor for Temperature Histograms')
    plt.get_current_fig_manager().window.state('zoomed')
    fig_4.tight_layout()
    plt.show()

# The solution to the 1st Bullet Point of 2 ##
# Calling the function "pmf" and setting as input the Temperature dataframes for each sensor.
# Generates the PMF bar graph
pmf(temp_a.astype(float),temp_b.astype(float),temp_c.astype(float),temp_d.astype(float),temp_e.astype(float))

### Probability Density function ###
def pdf(a,b,c,d,e):
    """Creates the PDF for the 5 sensors Temperature values.
    The variables a,b,c,d,e must be the dataframes of the sensors for the Temperature."""

    #Sets the figure
    fig_5= plt.figure(5)
    fig_5.canvas.set_window_title('PDF of the 5 sensor - Temperature Histogram')

    #Set axes in different subplot positions
    t_a=fig_5.add_subplot(231)
    t_b=fig_5.add_subplot(232)
    t_c=fig_5.add_subplot(233)
    t_d=fig_5.add_subplot(223)
    t_e=fig_5.add_subplot(224)
    
    #Generates the PDF's histogram + title
    t_a.hist(x=a,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85)
    t_a.set_title("Sens_A: PDF of temperature")
    t_b.hist(x=b,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85)
    t_b.set_title("Sens_B: PDF of temperature")
    t_c.hist(x=c,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85)
    t_c.set_title("Sens_C: PDF of temperature")
    t_d.hist(x=d,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85)
    t_d.set_title("Sens_D: PDF of temperature")
    t_e.hist(x=e,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85)
    t_e.set_title("Sens_E: PDF of temperature")   
    
    plt.suptitle('PDF of the 5 sensor for Temperature Histogram')
    plt.get_current_fig_manager().window.state('zoomed')
    fig_5.tight_layout()
    plt.show()

# The solution to the 1st Bullet Point of 2 ##
# Calling the function "pdf" and setting as input the Temperature dataframes for each sensor.
# Generates the PDF histogram.
pdf(temp_a.astype(float),temp_b.astype(float),temp_c.astype(float),temp_d.astype(float),temp_e.astype(float))

### Cumulative Density Function ###
def cdf(a,b,c,d,e):
    """Creates the CDF for the 5 sensors Temperature values.
    The variables a,b,c,d,e must be the dataframes of the sensors for the Temperature. """

    #Sets the figure and title
    fig_6 = plt.figure(6)
    fig_6.canvas.set_window_title('CDF of the 5 sensor - Temperature Histogram')

    #Sets axes in different subplot positions
    t_a=fig_6.add_subplot(231)
    t_b=fig_6.add_subplot(232)
    t_c=fig_6.add_subplot(233)
    t_d=fig_6.add_subplot(223)
    t_e=fig_6.add_subplot(224)

    #Generates the CDF's stepped histogram and c-line + title for each of the sensors.
    a1=t_a.hist(x=a,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85, density=True,histtype="step")
    t_a.plot(a1[1][1:]-(a1[1][1:]-a1[1][:-1])/2,a1[0], color='r')
    t_a.set_title("Sens_A: CDF of temperature")

    a2=t_b.hist(x=b,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    t_b.plot(a2[1][1:]-(a2[1][1:]-a2[1][:-1])/2,a2[0], color='r')
    t_b.set_title("Sens_B: CDF of temperature")

    a3=t_c.hist(x=c,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    t_c.plot(a3[1][1:]-(a3[1][1:]-a3[1][:-1])/2,a3[0], color='r')
    t_c.set_title("Sens_C: CDF of temperature")

    a4=t_d.hist(x=d,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    t_d.plot(a4[1][1:]-(a4[1][1:]-a4[1][:-1])/2,a4[0], color='r')
    t_d.set_title("Sens_D: CDF of temperature")

    a5=t_e.hist(x=e,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    t_e.plot(a5[1][1:]-(a5[1][1:]-a5[1][:-1])/2,a5[0], color='r')
    t_e.set_title("Sens_E: CDF of temperature")   
    
    plt.suptitle('CDF of the 5 sensor for Temperature Histogram')
    plt.get_current_fig_manager().window.state('zoomed')
    fig_6.tight_layout()
    plt.show()

# The solution to the 1st Bullet Point of 2 ##
# Calling the function "cdf" and setting as input the Temperature dataframes for each sensor.
# Generates the CDF histogram.
cdf(temp_a.astype(float),temp_b.astype(float),temp_c.astype(float),temp_d.astype(float),temp_e.astype(float))
#################################################################################################################################################################

#### 2nd Bullet Point of 2 -> For the Wind Speed values, plot the pdf and the kernel density estimation. ########################################################
# Comment the differences.

def pdf_kde(a,b,c,d,e):
    """Generates the PDF as the above function "pdf" and in addition, the KDE.
    The variables a,b,c,d,e must be the dataframes of the sensors for the Temperature."""

    #Sets the figure
    fig_7= plt.figure(7)
    fig_7.canvas.set_window_title('PDF and KDE of the 5 sensor - Wind Speed')

    #Sets axes in different subplot positions
    w_a=fig_7.add_subplot(231)
    w_b=fig_7.add_subplot(232)
    w_c=fig_7.add_subplot(233)
    w_d=fig_7.add_subplot(223)
    w_e=fig_7.add_subplot(224)

    #Generates the PDF's histogram and the KDE + title&axis labels for each of the sensors
    w_a.hist(x=a,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85)
    sns.distplot(a, color='y',ax=w_a, hist = True, kde=True)
    w_a.set_title("Sens_A: PDF and KDE of Wind Speed")
    w_a.set_xlabel('')

    w_b.hist(x=b,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85)
    sns.distplot(b, color='y',ax=w_b, hist = True, kde=True)
    w_b.set_title("Sens_B: PDF and KDE of Wind Speed")
    w_b.set_xlabel('')

    w_c.hist(x=c,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85)
    sns.distplot(c, color='y',ax=w_c, hist = True, kde=True)
    w_c.set_title("Sens_C: PDF and KDE of Wind Speed")
    w_c.set_xlabel('')

    w_d.hist(x=d,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85)
    sns.distplot(d, color='y',ax=w_d, hist = True, kde=True)
    w_d.set_title("Sens_D: PDF and KDE of Wind Speed")
    w_d.set_xlabel('')

    w_e.hist(x=e,bins=30, density=True, color='k',alpha=0.7, rwidth=0.85, label="PDF")
    sns.distplot(e, color='y',ax=w_e, hist = True,kde=True, label="KDE")
    w_e.set_title("Sens_E: PDF and KDE of Wind Speed")   
    w_e.set_xlabel('')
    w_e.legend(loc='upper right')
    
    plt.suptitle('PDF and KDE of the 5 sensor for Wind Speed')
    plt.get_current_fig_manager().window.state('zoomed')
    fig_7.tight_layout() 
    plt.show()

# The solution to the 2nd Bullet Point of 2 ##
# Calling the function "kde" and setting as input the Temperature dataframes for each sensor.
# Generates the KDE and PDF histogram.
pdf_kde(ws_a.astype(float),ws_b.astype(float),ws_c.astype(float),ws_d.astype(float),ws_e.astype(float))
#################################################################################################################################################################



######## FOR 3. AFTER LESSON A3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#### 1st Bullet Point of 3 -> Compute the correlations between all the sensors for the variables:
# Temperature, Wet Bulb Globe Temperature (WBGT), Crosswind Speed. 
# Perform correlation between sensors with the same variable, not between two different variables;
# for example, correlate Temperature time series between sensor A and B. 
# Use Pearson’s and Spearmann’s rank coefficients. Make a scatter plot with both coefficients with the 3 variables.

def corr(a,b,c,d,e):
    """Computes the Pearson's and Spearman's coefficients for the variables
    for 10 pairs of the 5 sensors and returns them as a dataframe with their corresponding sensor pair.
    The variables a,b,c,d,e must be dataframes of the variables in question. """

    #Interpolates the chosen pairs to equal size samples
    ab = np.interp(np.linspace(0,len(b),len(b)),np.linspace(0,len(a),len(a)),a)
    ac = np.interp(np.linspace(0,len(c),len(c)),np.linspace(0,len(a),len(a)),a)
    ad = np.interp(np.linspace(0,len(d),len(d)),np.linspace(0,len(a),len(a)),a)
    ae = np.interp(np.linspace(0,len(e),len(e)),np.linspace(0,len(a),len(a)),a)

    bc = np.interp(np.linspace(0,len(c),len(c)),np.linspace(0,len(b),len(b)),b)
    bd = np.interp(np.linspace(0,len(d),len(d)),np.linspace(0,len(b),len(b)),b)
    be = np.interp(np.linspace(0,len(e),len(e)),np.linspace(0,len(b),len(b)),b)

    cd = np.interp(np.linspace(0,len(d),len(d)),np.linspace(0,len(c),len(c)),c)
    ce = np.interp(np.linspace(0,len(e),len(e)),np.linspace(0,len(c),len(c)),c)

    de = np.interp(np.linspace(0,len(e),len(e)),np.linspace(0,len(d),len(d)),d)

    #Sets blank lists. p for pearson and s for spearman. The notion behind this is 
    #to grab the statics and append them to their respictive list for later use
    p=[]
    s=[]

    #Computes the coefficients and p-values from both methods.
    #Appends in the above lists, ONLY the coefficient and NOT the p-value. index[0]:coeff , index[1]:p-value.
    pcoef_ab = stats.pearsonr(ab,b)[0]
    prcoef_ab = stats.spearmanr(ab,b)[0]
    p.append(pcoef_ab)
    s.append(prcoef_ab)

    pcoef_ac = stats.pearsonr(ac,c)[0]
    prcoef_ac = stats.spearmanr(ac,c)[0]
    p.append(pcoef_ac)
    s.append(prcoef_ac)

    pcoef_ad = stats.pearsonr(ad,d)[0]
    prcoef_ad = stats.spearmanr(ad,d)[0]
    p.append(pcoef_ad)
    s.append(prcoef_ad)

    pcoef_ae = stats.pearsonr(ae,e)[0]
    prcoef_ae = stats.spearmanr(ae,e)[0]
    p.append(pcoef_ae)
    s.append(prcoef_ae)

    pcoef_bc = stats.pearsonr(bc,c)[0]
    prcoef_bc = stats.spearmanr(bc,c)[0]
    p.append(pcoef_bc)
    s.append(prcoef_bc)

    pcoef_bd = stats.pearsonr(bd,d)[0]
    prcoef_bd = stats.spearmanr(bd,d)[0]
    p.append(pcoef_bd)
    s.append(prcoef_bd)

    pcoef_be = stats.pearsonr(be,e)[0]
    prcoef_be = stats.spearmanr(be,e)[0]
    p.append(pcoef_be)
    s.append(prcoef_be)

    pcoef_cd = stats.pearsonr(cd,d)[0]
    prcoef_cd = stats.spearmanr(cd,d)[0]
    p.append(pcoef_cd)
    s.append(prcoef_cd)

    pcoef_ce = stats.pearsonr(ce,e)[0]
    prcoef_ce = stats.spearmanr(ce,e)[0]
    p.append(pcoef_ce)
    s.append(prcoef_ce)

    pcoef_de = stats.pearsonr(de,e)[0]
    prcoef_de = stats.spearmanr(de,e)[0]
    p.append(pcoef_de)
    s.append(prcoef_de)

    #1. Sets two dictionaries with the coefficients and the sensor pairs
    #2. Converts dictionary into pandas dataframes.
    #This was done to overcome inner compatabilty errors with seaborn library that is going to be used for plotting the scatterplot.
    dict1 = {'Coeff':p,'Sensor Pair':lista1}
    df_p=pd.DataFrame(dict1)

    dict2 = {'Coeff':s,'Sensor Pair':lista1}
    df_s=pd.DataFrame(dict2)

    #return the two dataframes containing the coefficient column and the pair column correctly matched. 
    return df_p,df_s

def corr_plt(T_a,T_b,T_c,T_d,T_e,W_a,W_b,W_c,W_d,W_e,C_a,C_b,C_c,C_d,C_e):
    """Plots the Pearson's and Spearman's coefficients for the variables Temperature,
    Wet Bulb Globe Temperature (WBGT) and Crosswind Speed for 10 pairs of the 5 sensors.
    The variables T_a,T_b,T_c,T_d,T_e,W_a,W_b,W_c,W_d,W_e,C_a,C_b,C_c,C_d,C_e must be the dataframes of the variables in question. 
    Calls the function "corr" to make the calculation of the correlation methods of Pearson and Spearman"""
    
    #Sets the figure and title
    fig_8= plt.figure(7)
    fig_8.canvas.set_window_title('Pearson-Spearman_5 sensors_Temp, WBGT,CrWinSpeed')

    #Sets axes in different subplot positions
    T_pear = fig_8.add_subplot(321)
    T_spear = fig_8.add_subplot(322)
    W_pear = fig_8.add_subplot(323)
    W_spear = fig_8.add_subplot(324)
    C_pear = fig_8.add_subplot(325)
    C_spear = fig_8.add_subplot(326)

    #Generates the scatter plots using function from the seaborn library.
    sns.stripplot(x="Sensor Pair", y="Coeff", data=corr(T_a,T_b,T_c,T_d,T_e)[0], ax= T_pear,color='c',size=10)
    sns.stripplot(x="Sensor Pair", y="Coeff", data=corr(T_a,T_b,T_c,T_d,T_e)[1], ax= T_spear,color='c',size=10)
    sns.stripplot(x="Sensor Pair", y="Coeff", data=corr(W_a,W_b,W_c,W_d,W_e)[0], ax= W_pear,color='b',size=10)
    sns.stripplot(x="Sensor Pair", y="Coeff", data=corr(W_a,W_b,W_c,W_d,W_e)[1], ax= W_spear,color='b',size=10)
    sns.stripplot(x="Sensor Pair", y="Coeff", data=corr(T_a,T_b,T_c,T_d,T_e)[0], ax= C_pear,color='k',size=10)
    sns.stripplot(x="Sensor Pair", y="Coeff", data=corr(C_a,C_b,C_c,C_d,C_e)[1], ax= C_spear,color='k',size=10)
    
    #Sets labels and title. 
    T_pear.set_xlabel("")
    T_pear.set_ylabel('|------------- Temperature ---------|'+"\n\n\n"+"Pearson correlation")
    T_spear.set_xlabel('')
    T_spear.set_ylabel("Spearman correlation")
    
    W_pear.set_xlabel('')
    W_pear.set_ylabel('|--------------- WBGT ----------------|'+"\n\n\n"+"Pearson correlation",labelpad=10.5)
    W_spear.set_xlabel('')
    W_spear.set_ylabel("Spearman correlation")
    
    C_pear.set_xlabel('Sensor - Pairs')
    C_pear.set_ylabel('|------- Cross wind speed --------|'+"\n\n\n"+"Pearson correlation")
    C_spear.set_xlabel('Sensor - Pairs')
    C_spear.set_ylabel("Spearman correlation")
    
    plt.suptitle("Pearson and Spearman Correlations between the 5 sensors for Temperature, Wet Bulb Global Temperature and Cross Wind Speed")
    plt.get_current_fig_manager().window.state('zoomed')
    #fig_8.tight_layout()
    plt.show()

## The solution to the 1st Bullet Point of 3 ##
# Calling the function "corr_plt" and setting as input the dataframes for each sensor for the 3 variables
#Temperature, Wet Bulb Globe Temperature (WBGT), Crosswind Speed.
corr_plt(temp_a.astype(float),temp_b.astype(float),temp_c.astype(float),temp_d.astype(float),temp_e.astype(float),
wbg_a.astype(float),wbg_b.astype(float),wbg_c.astype(float),wbg_d.astype(float),wbg_e.astype(float),
cws_a.astype(float),cws_b.astype(float),cws_c.astype(float),cws_d.astype(float),cws_e.astype(float))
#################################################################################################################################################################



######## FOR 4. AFTER LESSON A4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#### 1st Bullet Point of 4 ->
def cdf_(a,b,c,d,e,z,y,x,w,u):
    """Creates the CDF for the 5 sensors Temperature values for the variables Temperature and Wind Speed.
    The variables a,b,c,d,e must be the dataframes of the sensors for the Temperature.
    The variables z,y,x,w,u must be the dataframes of the sensors for the Wind Speed.
    The function works the same as "cdf" from above """

    #Sets figure and title
    fig_9= plt.figure(9)
    fig_9.canvas.set_window_title('CDF of the 5 sensor - Temperature, Wind Speed')
    
    #Sets axes in different subplot positions and removes extra redundunt ticks from the y axis.
    t_a=fig_9.add_subplot(251)
    t_b=fig_9.add_subplot(252)
    t_c=fig_9.add_subplot(253)
    t_d=fig_9.add_subplot(254)
    t_e=fig_9.add_subplot(255)
    t_b.axes.yaxis.set_ticks([])
    t_c.axes.yaxis.set_ticks([])
    t_d.axes.yaxis.set_ticks([])
    t_e.axes.yaxis.set_ticks([])
    
    ws_a=fig_9.add_subplot(256)
    ws_b=fig_9.add_subplot(257)
    ws_c=fig_9.add_subplot(258)
    ws_d=fig_9.add_subplot(259)
    ws_e=fig_9.add_subplot(2,5,10)
    ws_b.axes.yaxis.set_ticks([])
    ws_c.axes.yaxis.set_ticks([])
    ws_d.axes.yaxis.set_ticks([])
    ws_e.axes.yaxis.set_ticks([])


     #Generates the CDF's stepped histogram and c-line + title for each of the sensors for the variables Temperatue and Wind Speed.
    a1=t_a.hist(x=a,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    t_a.plot(a1[1][1:]-(a1[1][1:]-a1[1][:-1])/2,a1[0], color='r')
    t_a.set_title("Sens_A: CDF of temperature")

    a2=t_b.hist(x=b,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    t_b.plot(a2[1][1:]-(a2[1][1:]-a2[1][:-1])/2,a2[0], color='r')
    t_b.set_title("Sens_B: CDF of temperature")

    a3=t_c.hist(x=c,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    t_c.plot(a3[1][1:]-(a3[1][1:]-a3[1][:-1])/2,a3[0], color='r')
    t_c.set_title("Sens_C: CDF of temperature")

    a4=t_d.hist(x=d,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    t_d.plot(a4[1][1:]-(a4[1][1:]-a4[1][:-1])/2,a4[0], color='r')
    t_d.set_title("Sens_D: CDF of temperature")

    a5=t_e.hist(x=e,bins=30, cumulative=True, color='g',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    t_e.plot(a5[1][1:]-(a5[1][1:]-a5[1][:-1])/2,a5[0], color='r')
    t_e.set_title("Sens_E: CDF of temperature")   


    w1=ws_a.hist(x=z,bins=30, cumulative=True, color='k',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    ws_a.plot(w1[1][1:]-(w1[1][1:]-w1[1][:-1])/2,w1[0], color='r')
    ws_a.set_title("Sens_A: CDF of Wind Speed")

    w2=ws_b.hist(x=y,bins=30, cumulative=True, color='k',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    ws_b.plot(w2[1][1:]-(w2[1][1:]-w2[1][:-1])/2,w2[0], color='r')
    ws_b.set_title("Sens_B: CDF of Wind Speed")

    w3=ws_c.hist(x=x,bins=30, cumulative=True, color='k',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    ws_c.plot(w3[1][1:]-(w3[1][1:]-w3[1][:-1])/2,w3[0], color='r')
    ws_c.set_title("Sens_C: CDF of Wind Speed")

    w4=ws_d.hist(x=w,bins=30, cumulative=True, color='k',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    ws_d.plot(w4[1][1:]-(w4[1][1:]-w4[1][:-1])/2,w4[0], color='r')
    ws_d.set_title("Sens_D: CDF of Wind Speed")

    w5=ws_e.hist(x=u,bins=30, cumulative=True, color='k',alpha=0.7, rwidth=0.85,density=True,histtype="step")
    ws_e.plot(w5[1][1:]-(w5[1][1:]-w5[1][:-1])/2,w5[0], color='r')
    ws_e.set_title("Sens_E: CDF of Wind Speed") 
    
    
    plt.suptitle('CDF of the 5 sensor for Temperature and Wind Speed Histograms')
    plt.get_current_fig_manager().window.state('zoomed')
    fig_9.tight_layout()
    plt.show()

# The solution to the 1st Bullet Point of 4 ##
# Calling the function "cdf" and setting as input the Temperature dataframes for each sensor.
# Generates the CDF histogram.
cdf_(temp_a.astype(float),temp_b.astype(float),temp_c.astype(float),temp_d.astype(float),temp_e.astype(float),
df_a[lista[1]].astype(float), df_b[lista[1]].astype(float),df_c[lista[1]].astype(float),df_d[lista[1]].astype(float),df_e[lista[1]].astype(float))
#################################################################################################################################################################

### The below code is deactivated because whenever it runs is appends values into the created file "cofidence.txt".
'''
def inte(a,b,c,d,e):
    """Computes the 95% confidence intervals for variables Temperature and Wind Speed for all the sensors and saves them into csv format.
    The variables a,b,c,d,e must be dataframes of the variables """ 

    report=open("confidence.txt","a")
    
    report.write("~~~~~~~~~~~~~~~~~~~"+"\n"+ str(stats.t.interval(0.95, len(a)-1, loc=np.mean(a), scale=stats.sem(a))[0]) +" , " + str(stats.t.interval(0.95, len(a)-1, loc=np.mean(a), scale=stats.sem(a))[1])+"\n")
    report.write(str(stats.t.interval(0.95, len(b)-1, loc=np.mean(b), scale=stats.sem(b))[0]) +" , " +str(stats.t.interval(0.95, len(b)-1, loc=np.mean(b), scale=stats.sem(b))[1])+"\n")
    report.write(str(stats.t.interval(0.95, len(c)-1, loc=np.mean(c), scale=stats.sem(c))[0]) +" , " + str(stats.t.interval(0.95, len(c)-1, loc=np.mean(c), scale=stats.sem(c))[1])+"\n")
    report.write(str(stats.t.interval(0.95, len(d)-1, loc=np.mean(d), scale=stats.sem(d))[0]) +" , "  +str(stats.t.interval(0.95, len(d)-1, loc=np.mean(d), scale=stats.sem(d))[1])+"\n")
    report.write(str(stats.t.interval(0.95, len(e)-1, loc=np.mean(e), scale=stats.sem(e))[0]) +" , "  +str(stats.t.interval(0.95, len(e)-1, loc=np.mean(e), scale=stats.sem(e))[1])+"\n")
   
    report.close()

#compute the 95% confidence intervals for variables Temperature and Wind Speed for all the sensors and save them in a table
inte(df_a[lista[1]].astype(float),df_b[lista[1]].astype(float),df_c[lista[1]].astype(float),df_d[lista[1]].astype(float),df_e[lista[1]].astype(float))
inte(df_a[lista[4]].astype(float),df_b[lista[4]].astype(float),df_c[lista[4]].astype(float),df_d[lista[4]].astype(float),df_e[lista[4]].astype(float))
'''
#################################################################################################################################################################

### The below code is deactivated because whenever it runs is appends values into the created file "hypothesis.txt".
'''
def pval(a,b):
    """ Computes and returns the t and p values using the "ttest".
    The variables a and b are the dataframes"""

    data=a,b
    t, p = stats.ttest_ind(data[0],data[1])
    return t, p 

def file(a,b):
    """Writes the p-value into the "hypothesis.txt"
    The variables a and b are the dataframes"""

    values=open("hypothesis_p_only.txt","a")

    values.write(str(pval(a,b)[1])+"\n")

    values.close()

# The solution to the 2st Bullet Point of 4 ##
# Calling the funtion "file" setting as intput the dataframes of Temperature and Wind Speed.
file(temp_e.astype(float).values,temp_d.astype(float).values)
file(temp_d.astype(float).values,temp_c.astype(float).values)
file(temp_c.astype(float).values,temp_b.astype(float).values)
file(temp_b.astype(float).values,temp_a.astype(float).values)
    
file(ws_e.astype(float).values,ws_d.astype(float).values)
file(ws_d.astype(float).values,ws_c.astype(float).values)
file(ws_c.astype(float).values,ws_b.astype(float).values)
file(ws_b.astype(float).values,ws_a.astype(float).values)
'''
#################################################################################################################################################################
############ END ###############################################################################################################################################