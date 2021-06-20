# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:36:59 2020

@author: intel
"""
import requests
import smtplib 

# API key
#api_file = open("api key.txt", "r")
api_key = "eXSEsT6TdxudAqJfZ5kk2TjPbFd4h"
#api_file.close()

# home address input
home = input("Enter a current address\n") 
  
# work address input
work = input("Enter a work address\n") 
  
# base url
url = "https://api.distancematrix.ai/maps/api/distancematrix/json?"

# get response
r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key) 
 
# return time as text and as seconds

time = r.json()["rows"][0]["elements"][0]["duration"]["text"] 
      
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

  
# print the travel time
print("\nThe total travel time from home to work is", time)




#code for mailing


# check if travel time is more than .5 hour

if (seconds < 1800):
    print("you have enough time.")
if (seconds > 1800):
    # email constraints
    sender = "honeyagrawal929@gmail.com"    
    recipient = "hiteshagrawal510@gmail.com"       
    subject = "Got stuck in traffic"   
    message = "Good Morning sir,\n\nSorry, I can't make it on time today."
    
    # format email
    email = "Subject: {}\n\n{}".format(subject, message)
    
    # get sender password
   # password_file = open("password.txt", "r")
   # password = password_file.readline()
   # password_file.close()
    
    # creates SMTP session 
    s = smtplib.SMTP("smtp.gmail.com", 587) 
      
    # start TLS for security 
    s.starttls() 
      
    # authentication 
    s.login(sender, "hiitesh123.") 
      
    # sending the mail 
    s.sendmail(sender, recipient, email)
    
    
      
    # terminating the session 
    s.quit() 
   

    # success message
    print("\nSuccessfully sent an email to", recipient, "\n  since the travel time was too long!")