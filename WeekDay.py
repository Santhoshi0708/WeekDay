import streamlit as srt #A library to easify the user without requiring front end knowledge
import datetime # A builtin module to use date related builtin functions
import calendar # A builtin module to use calendar related functions

#To represent the tile to our web page
str.title("WeekDay Using streamlit")
Input_date=srt.date_input("Enter DateInput",min_value=datetime.date(1800,1,1),max_value=datetime.date(2100,1,1))
#Days of a week
Weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
year=Input_date.year
month=Input_date.month
day=Input_date.day
#A value which shows the weekDay 
Datevalue=calendar.weekday(year,month,day)
WeekDay_result=Weekdays[Datevalue]
srt.write("The Week Day is:",WeekDay_result)
