# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:49:09 2020

@author: devag
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="zides"
)
mycursor=mydb.cursor()
mycursor.execute('Create database student')

