GEO1001 - Assignment 1 

The current repository contains all the files related to the 1st assignment for the course GEO1001.
The structure of the respository is as follows:

-The directory 'Graph' contains all of the figures and images that are used in the report as .png files

-The directory hw01 contains all the necessary data that were used in the code. 

-The file 'BonusQuestion.py' is a secondary python file thas is used to answer the bonus question.

-The file Hw01_PANTELIOS_KONSTANTINOS.pdf is the Final report of the excerise in PDF from generated through LaTeX.

-The file Hw01_LaTeX.tex is the LaTeX code that generates the final report (the pdf file above).

-The file 'README.md' is the current file containing the instructions.

-The file 'confidence.txt' contains the 95% confidence intervals for variables Temperature and Wind Speed for all the sensors.

-The file 'geo1001_hw01.py' is the main code of the excerice for the 4 parts (the bonus questions is in file 'BonusQuestion.py')

-The file 'hypothesis_p_only.txt' contains the p-values of Temperature and Winds speed for sensor pairs specified in part 4.2

-The file reference.bib is used by the file Hw01_LaTeX.tex to introduce the citation of the data that were used to complete the assignment.



              Explaining the main code 'geo1001_hw01.py' and additional code 'BonusQuestion.py'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!Inside the code there are multiple commnets to help the reader understand the reasoning of it.

!The code runs and starts printing and plotting in an ascending order in respect to the 4 parts of the assignments.

!The code stops running after plotting any figure -> To continue, please close the opened figure.

!You can safely diregard any waring message from matplotlib. The overlapping figures produce these warning but they don't halt or affect the code in any way.

0.1 First of all before takling any of the questions, the code import necessary libraries(from local environment)
and data from the directory 'hw01'

0.2 Next comes the creation of multiple dataframes that are used later in the code, using pandas libraries.
In detail: variables that contain the characters a,b,c,d and e correspond to the same kind of variable but with different values. a,b,c,d and
e represent the 5 different sensors.

temp_a == dataframe of Temperature of sensor A
temp_b == dataframe of Temperature of sensor B
temp_c == dataframe of Temperature of sensor C
temp_d == dataframe of Temperature of sensor D
temp_e == dataframe of Temperature of sensor E

ws_a == dataframe of Wind Speed of sensor A
ws_b == dataframe of Wind Speed of sensor B
ws_c == dataframe of Wind Speed of sensor C
ws_d == dataframe of Wind Speed of sensor D
ws_e == dataframe of Wind Speed of sensor E

wd_a == dataframe of Wind Direction , True of sensor A
wd_b == dataframe of Wind Direction , True of sensor B
wd_c == dataframe of Wind Direction , True of sensor C
wd_d == dataframe of Wind Direction , True of sensor D
wd_e == dataframe of Wind Direction , True of sensor E

cws_a == dataframe of Cross Wind Speed of sensor A
cws_b == dataframe of Cross Wind Speed of sensor B
cws_c == dataframe of Cross Wind Speed of sensor C
cws_d == dataframe of Cross Wind Speed of sensor D
cws_e == dataframe of Cross Wind Speed of sensor E

wbg_a == dataframe of Wet Bulb Globe Temperature of sensor A
wbg_b == dataframe of Wet Bulb Globe Temperature of sensor B
wbg_c == dataframe of Wet Bulb Globe Temperature of sensor C
wbg_d == dataframe of Wet Bulb Globe Temperature of sensor D
wbg_e == dataframe of Wet Bulb Globe Temperature of sensor E

1.1 For this part the code uses the function 'statistics' which computes Mean, Variance and Standard deviation.
A 'for' loop is used to iterate through the sensors calling the fucntion for each variable.

1.2 For this part the code utilizes the function 'hist_temp' which Creates the 2 Temperature histograms 
of different bin numers for all of the sensors. it takes as inputs the temperature dataframes and the bins to compare.

1.3 For this part the code calls the function 'hist_temp_sens' which generates an overlapping plot of friquency 
polygons for the Temperature of 5 sensors. It takes as inputs the dataframes of the temperature. 

1.4 For this part the code generates the boxplot figures fot the Temperature, Wind Speed and Wind Direction, through the fucntiion
'boxplt'. The function takes as inputs all of the dataframes of the abovementioned variables

2.1 For this section the code utilizes two function to plot the probability mass function figure of the Temperature. 'pmf_2' which makes the calculations and 'pmf' which plots the figure. As inputs they accept the dataframes of the Temperature.
To plot the probability density function the code uses the function 'pdf' which takes as inpute the dataframes of the Temperature
To plot the cumulative density function the code uses the fucntion 'cdf'. Like pdf, it takes the dataframes of the Temperature as inputs.

2.2 For this part the code runs the function 'pdf_kde' which generates the PDF as the above function "pdf" and in addition, the kernel density estimation. It takes as inputs the dataframes of the Temperature.

3.1 For this part the code uses fucntion 'corr_plt' (to plot the figure of the correlations) which is linked to the fucntion 'corr' which is thefunction that computes and returns the coefficients. As inputs it they take the dataframes of the Temperature, the Wet Bulb Globe Temperature and the Cross Wind Speed.

4.1 For this part the code calls the function 'cdf_' which is a modified fucntion of the above 'cdf'. It plots the CDF for both Temperature and Wind Speed variable. It takes as inputs their dataframes.

||||__Attention for the next part__||||
The function 'inte' computes the 95% confidence intervals for the variables Temperature and Wind Speed and APPENDS them into the file 'confidence.txt'. It takes as inputs the dataframes of the variables
The function 'pval' and 'file' are connected to each other. 'pval' execute the ttest function and returen the t and p values. 'file' APPENDS the p-value into the file 'hypothesis_p_only.txt'. The function accept as inputs the dataframe of the above variables but only for the specific pair of sensor each time (the pairs are specified in part 4.2).

Ii is IMPORTANT NOT to run these batches of code as the append attribute WONT overwrite the previous values.
For these reason these lines of code have been deactivated.
||||||||||||||||||||||||||||||||||||||||

For the bonus question the dataframes in use are:

ttemp_a == dataframe of FORMATTED DATE-TIME and Temperature of sensor A
ttemp_b == dataframe of FORMATTED DATE-TIME and Temperature of sensor B
ttemp_c == dataframe of FORMATTED DATE-TIME and Temperature of sensor C
ttemp_d == dataframe of FORMATTED DATE-TIME and Temperature of sensor D
ttemp_e == dataframe of FORMATTED DATE-TIME and Temperature of sensor E
Other dataframes are created in the code for better use

The function 'data' groups the measumermnts by days and calculates and returns the mean Temperature. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For more information about the fucntions' inner workings see comments inside the code.
  
