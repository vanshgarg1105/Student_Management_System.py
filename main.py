#import libraries   ----> These are the libraries that we are going to import
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

#functions to define database
def Database():
  global conn , cursor
  #creating student database
  conn = sqlite3.connect("student.db")
  cursor = conn.cursor()
  #creating Stud_Registration table
  cursor.execute(
    "CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT)")
