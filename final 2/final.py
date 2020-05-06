# -*- coding: utf-8 -*-
"""


@author: alexander.harrison
"""

#importing libraray for use within code
import csv
import matplotlib.pyplot as plt
import numpy as np

#making a function
def processJailCSV():
    """


 Data used in this file was taken from: https://data.wprdc.org/dataset/allegheny-county-jail-daily-census/resource/1e9b0886-5756-413a-b35f-89746cf56fd9

    """
   
   #opening file
    file = open('acj.csv', newline='')
    #making a reader
    reader = csv.DictReader(file)
    #setting up the dictionary and adding to assests to it
    raceCount = {'B':0, 'W':0}
    genderCount = {'F':0, 'M':0}
    ageAtBooking=[]
    ageNow=[]
    femaleCount=[]
    maleCount=[]

    

    #setting focusDate for if statement below
    focusDate = '6/1/2019'
   
   #for loop to check rows over and over
    for row in reader:
       
       #if date in row within the data sheet matches focusDate, carry into next if statement
        if row['Date'] == focusDate:
            ageAtBooking.append(row['Age at Booking'])
            ageNow.append(row['Current Age'])
            ageAtBooking = [int(i) for i in ageAtBooking]
            ageNow = [int(i) for i in ageNow]
            # if row Race equals B
            if row['Race'] == 'B':
                #add 1 to B race
                raceCount['B'] = raceCount['B'] + 1
            # if row Race equals A
            elif row['Race']  == 'W':
                # add 1 to W Race
                raceCount['W'] = raceCount['W'] + 1
            if row['Gender'] == 'F':
                genderCount['F'] = genderCount['F'] + 1
            elif row['Gender'] == 'M':
                genderCount['M'] = genderCount['M'] + 1
    allInmates = raceCount['B'] + raceCount['W']
    femaleCount.append(genderCount['F'])
    maleCount.append(genderCount['M'])
    
    #ageNowA = sum(ageNow)
    #ageBookingA = sum(ageAtBooking)
    #print(maleCount, femaleCount)
    #print(genderCount['M'], genderCount['F'])
    #print(allInmates)
 
            
    
    objects = ('Females', 'Males', 'All Inmates')
    y_pos = np.arange(len(objects))
    performance = genderCount['F'], genderCount['M'],  allInmates

    plt.barh(y_pos, performance, align='center', alpha=1)
    plt.yticks(y_pos, objects)
    plt.title('Allgheny County Jail Inmates')

    plt.show()       
           
        
                             




    #closes file     
    file.close()
   
  
    

processJailCSV()
