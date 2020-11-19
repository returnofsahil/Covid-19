# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:36:10 2020

@author: devag
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 
import mysql.connector as conn
global df
df=pd.read_csv(r"C:\\Users\\devag\\Downloads\\full_data.csv")
#function to display main menu

def main_menu():
    print("**********************************")
    print("Read data from file in different way")
    print("1.read complete csv file")
    print("2.reading complete file without index")
    print("================")
    print("Data Visualization")
    print("3.Line chart")
    print("4.Bar plot")
    print("5.Pie chart")
    print("6.Scatter chart")
    print("================")
    print("Apply data manipulation in the records of csv files")
    print("7.Sorting the data as per your choice")
    print("8.Read top and bottom records from file as per requirement")
    print("9.Make the copy of CSV file")
    print("10.Read the Specific columns")
    print("************************************")
    
main_menu()

def ReadCSV():
    print("Reading data from CSV file")
    df=pd.read_csv(r"C:\users\devag\Downloads\raw_data16")
    print (df)
    