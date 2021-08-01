# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 10:03:05 2021

@author: Liam O'Connor
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


df = pd.read_csv(filepath)  #pandas library reads file into a data frame
print(df)       #prints the data frame 




if STRESSSTATE >= 75:
    print("The child is highly stressed")
elif (STRESSSTATE < 75 and STRESSSTATE >=50):
    print ("The child is moderatley stressed out")
else:
    print ("The child is not noticeably stressed out")