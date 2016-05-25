# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:12:59 2016

@author: visethsen
"""
#Imports two modules allowing them to be called/used
import webbrowser
import time

#Set the Variables:
total_breaks = 3
break_count = 0


#The Window will pop up with nba.com every 5 seconds
#Change amount in time.sleep(x) : Currently set to 20 minutes
#Change site in webbrowser.open(x)
while(break_count< total_breaks):
    time.sleep(1200)
    webbrowser.open("https://www.youtube.com/watch?v=R_CYkvXdYXE")
    break_count=break_count+1
    #Count Goes up 1    
    print ('this program started on ' +time.ctime())
    print ("break count is = " + str(break_count))

#Celebrate after 1 Hour of hard work    
webbrowser.open("https://www.youtube.com/watch?v=y6Sxv-sUYtM")
    
    
