# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 10:03:05 2021

@authors: Liam O'Connor, Hiranya Maharaja
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

filepath = 'SampleCSVFile_2kb.csv'  #File containing EEG data we want to open and monitor
STRESSSTATE = 0     #global variable for stress level as percentage


df = pd.read_csv(filepath)
print(df)




if STRESSSTATE >= 75:
    print("The child is highly stressed")
elif (STRESSSTATE < 75 and STRESSSTATE >=50):
    print ("The child is moderatley stressed out")
else:
    print ("The child is not noticeably stressed out")