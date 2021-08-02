# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 10:03:05 2021

@author: Liam O'Connor, Hiryana Maharaja, Harleen Kaur, and Jenny Wei
"""
import sys
from math import sqrt, acos, pi, sin
import matplotlib.pyplot as plt
import matplotlib

import numpy as np
import time
import csv
import os
import pandas as pd
import sqlite3
from scipy import fft

filepath = 'C:\python\PyQt5\SampleCSVFile_2kb.csv'  #File containing EEG data we want to open and monitor
STRESSSTATE = 0     #global variable for stress level as percentage
RUNCONDITION = True #variable to keep loop running based on user input
PlottingList =[]

df = pd.read_csv(filepath)  #pandas library reads file into a data frame
i=0         #variable toiterate through lines of csv file
try:            #try loop to allow keyboard interrupt to terminate program
    while RUNCONDITION:
        #print(df)       #prints the data frame 
        print(i)
        print(df.iat[i,1]) #df.iat returns the value at given indices
        
        STRESSSTATE = df.iat[i,1] #update the stressstate (frequency hopefully) to the new line in file.
        PlottingList.append(STRESSSTATE)
        print("plotting list = " + str(PlottingList[i]))
        
        if STRESSSTATE >= 75:
            print("The child is highly stressed")
        elif (STRESSSTATE < 75 and STRESSSTATE >=50):
            print ("The child is moderatley stressed out")
        else:
            print ("The child is not noticeably stressed out")
        #plt.plot(i,STRESSSTATE, 'ro') #plots current data of loop only
        plt.plot(PlottingList)
        plt.axis([0,50,0,100])
        plt.xlabel('Time')
        plt.ylabel('Frequency (Hz)')
        plt.show()           
        if i==16:          #set to number of lines in file to end loop without keyboard interrupt
           break
        i += 1
except KeyboardInterrupt:           #key input should pause loop and allow termination
    print("Press Ctrl-C to terminate the program/loop.")
    pass
