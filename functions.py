import pandas as pd 
import numpy as np
import datetime
import time
import matplotlib.pyplot as plt
import seaborn
import math

# Reading and cleaning the data
sleep = pd.read_excel('circanlog.xlsx')
#Converting format of columns to [datetime64]
sleep['Days'] = pd.to_datetime(sleep['Days'])
sleep['Wake'] = pd.to_datetime(sleep['Wake'])
sleep['Sleep'] = pd.to_datetime(sleep['Sleep'])
sleep.dropna(inplace = True)
#New column which shows name of day
sleep['Weekday'] = sleep['Days'].dt.day_name()

#New column which states the number of hours slept
sleep['Hours of Sleep'] = (abs(sleep['Sleep'] -sleep['Wake']))
#Converting it to hours and rounding it to 2 decimals
sleep['Hours of Sleep'] = sleep['Hours of Sleep']/np.timedelta64(1,'h')
sleep['Hours of Sleep'] = round(sleep['Hours of Sleep'], 2)
sleep['Hours of Sleep'] = sleep['Hours of Sleep'] - sleep['Naps']

############################### DATA CLEANING COMPLETE #########################################################
#Mean & Deviation of Mood and Sleep
avgmood = (round(sleep['Mood'].mean(), 2))
avgsleep = (round(sleep['Hours of Sleep'].mean(), 2))
devmood = (round(sleep['Mood'].std(), 2))
devsleep = (round(sleep['Hours of Sleep'].std(), 2))

#Making a new dataframe of only weekends
weekends = [sleep[sleep['Weekday'] == 'Saturday'], sleep[sleep['Weekday'] == 'Sunday']]
weekends = pd.concat(weekends)
weekends.sort_index(inplace = True)

#Making a new dataframe of only weekdays
wkdys = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekdays = sleep[sleep['Weekday'].isin(wkdys)]
weekdays.sort_index(inplace = True)

#Mean relations of weekends 
avgweekends = (round(weekends['Hours of Sleep'].mean(), 2))
moodweekends = (round(weekends['Mood'].mean(), 2))

#Mean relations of weekdays
avgweekdays = (round(weekdays['Hours of Sleep'].mean(), 2))
moodweekdays = (round(weekdays['Mood'].mean(), 2))

############################### DATA ANALYSING COMPLETE #########################################################

#Plotting the relations
def plot():
    seaborn.set()
    plt.figure('Sleep Analysis', figsize=(9,7))
    plt.subplot(311)
    plt.axhline(y=15000, color='g', linestyle=':')
    plt.plot(sleep.index, sleep['Steps'], 'g', label = 'Steps')
    plt.xlabel("Days") 
    plt.ylabel("Stepcount") 
    ax = plt.gca()
    ax.legend(loc = 'upper left')

    plt.subplot(312)
    plt.axhline(y=8.0, color='b', linestyle=':')
    plt.axhline(y=2.0, color='r', linestyle=':')
    plt.plot(sleep.index, sleep['Mood'], 'r', label = 'Mood')
    plt.plot(sleep.index, sleep['Hours of Sleep'], 'b', label = 'Hours of Sleep')
    plt.xlabel("Days") 
    plt.ylabel("Average Hours of Sleep") 
    ax = plt.gca()
    ax.legend(loc = 'upper left')

    if math.isnan(avgweekdays) or math.isnan(avgweekends) is False:
        plt.subplot(313)
        data = {'Weekdays': avgweekdays, 'Weekends': avgweekends}
        day = list(data.keys())
        average = list(data.values())
        plt.bar(day, average, color = 'maroon', width = 0.1)
        plt.xlabel("Days of the Week") 
        plt.ylabel("Average Hours of Sleep") 
    elif math.isnan(avgweekdays) or math.isnan(avgweekends) is True:
        pass
    
    return plt.show()

