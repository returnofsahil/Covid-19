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

# function to display main menu


def main_menu():
    print("**********************************")
    print("Read data from file in different way")
    print("1.read complete csv file")
    print("2.reading complete file without index")
    print("================")
    print("Data Visualization")
    print("3.Line chart")
    print("4.Bar plot")

    print("================")

    print("5.Sorting the data as per your choice")
    print("6.Read top  records from file as per requirement")
    print("7.Read bottom records from file as per requirement")

    print("************************************")
  # def is used to create a function .Function is a piece of code that can be executed again

# this function is used to create a csv file


def ReadCSV():
    print("Reading data from CSV file")
    df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')
    print(df)


def no_index():
    """
    reading without index
    """
    print('Reading Data from CSV file without index value')
    df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv', index_col=0)
    print(df)


def line_plot():
    df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')
    st = df['State']
    cnf = df['Confirmed']
    rc = df['Recovered']
    dth = df['Deaths']
    ac = df['Active']
    plt.xlabel('state')
    plt.xticks(rotation='vertical')

    print('Select Specific Line Chart as Given below:')
    print('press 1 to print the data  State vs Confirmed Cases')
    print('press 2 to print the data for State vs Recovered Cases')
    print('press 3 to print the data for State Vs Death Cases')
    print('press 4 to print the data for State Vs Active Cases')
    print("press 5 to merge all in one Line Chart")

    op = int(input("Enter your Choice"))

    if op == 1:
        plt.ylabel('Confirmed cases')
        plt.title('State vs Confirmed')
        plt.plot(st, cnf)
        plt.show()
    elif op == 2:
        plt.ylabel('Recovered cases')
        plt.title('State wise confirmed')
        plt.plot(st, rc)
        plt.show()
    elif op == 3:
        plt.ylabel('Death cases')
        plt.title('State wise Death Cases')
        plt.plot(st, dth)
        plt.show()
    elif op == 4:
        plt.ylabel('Active cases')
        plt.title('State wise Active Cases')
        plt.plot(st, ac)
        plt.show()

    elif op == 5:
        plt.ylabel("No of cases")
        plt.plot(st, cnf, label="State wise Confirmed")
        plt.plot(st, rc, label='state wise recovered')
        plt.plot(st, dth, label="state wise death")
        plt.plot(st, ac, label="state wise Active Cases")
        plt.legend()
        plt.show()
    else:
        print('Enter valid input')


def bar_plot():
    df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')
    st = df['State']
    cnf = df['Confirmed']
    rc = df['Recovered']
    dth = df['Deaths']
    ac = df['Active']
    plt.xlabel('state')
    plt.xticks(rotation='vertical')

    print('Select Specific Line Chart as Given below:')
    print('press 1 to print the data  State vs Confirmed Cases')
    print('press 2 to print the data for State vs Recovered Cases')
    print('press 3 to print the data for State Vs Death Cases')
    print('press 4 to print the data for State Vs Active Cases')
    print("press 5 to merge all in stack bar chart")

    op = int(input("Enter your Choice"))

    if op == 1:
        plt.ylabel('Confirmed cases')
        plt.title('State vs Confirmed')
        plt.bar(st, cnf)
        plt.show()
    elif op == 2:
        plt.ylabel('Recovered cases')
        plt.title('State wise confirmed')
        plt.bar(st, rc)
        plt.show()
    elif op == 3:
        plt.ylabel('Death cases')
        plt.title('State wise Death Cases')
        plt.bar(st, dth)
        plt.show()
    elif op == 4:
        plt.ylabel('Active cases')
        plt.title('State wise Active Cases')
        plt.bar(st, ac)
        plt.show()

    elif op == 5:
        plt.ylabel("No of cases")
        plt.bar(st, cnf, label="State wise Confirmed")
        plt.bar(st, rc, label='state wise recovered')
        plt.bar(st, dth, label="state wise death")
        plt.bar(st, ac, label="state wise Active Cases")
        plt.legend()
        plt.show()
    else:
        print('Enter valid input')


def data_sorting():
    print('Press 1 to arrange the record as per the State Name')
    print('Press 2 to arrange the record as per the Confirmed Cases')
    print('Press 3 to arrange the record as per the Recovered Cases')
    print('Press 4 to arrange the record as per the Total Death')
    print('Press 5 to arrange the record as per the Active Cases')

    op = int(input("Enter Your Choice"))
    if op == 1:
        df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')
        df.sort_values(["State"], inplace=True)
        # inplace makes the change in df
        print(df)
    elif op == 2:
        df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')

        df.sort_values(["Confirmed"], inplace=True)
        print(df)
    elif op == 3:
        df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')
        df.sort_values(["Recovered"], inplace=True)
        print(df)
    elif op == 4:
        df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')
        df.sort_values(["Deaths"], inplace=True)
        print(df)
    elif op == 5:
        df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')
        df.sort_values(["Active"], inplace=True)
        print(df)


def top_selected():
    df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')
    top = int(input("How many records  from top to display"))
    print('1st', top, "records")
    print(df.head(top))


def bottom_selected():
    df = pd.read_csv('C:/Users/DELL/Downloads/state_wise.csv')
    bottom = int(input("How many records  from bottom to display"))
    print('1st', bottom, "records")
    print(df.tail(bottom))


opt = int(input("Enter Your Choice"))
if opt == 1:
    ReadCSV()
if opt == 2:
    no_index()
elif opt == 3:
    line_plot()
elif opt == 4:
    bar_plot()
elif opt == 5:
    data_sorting()
elif opt == 6:
    top_selected()
elif opt == 7:
    bottom_selected()
