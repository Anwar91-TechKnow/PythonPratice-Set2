#             ANWAR SHAIKH
#             Python program set2/007
#             Title: Finding URLs from string
'''This program help us to find single or multiple URL which are present
in thes string value.
============================================================
'''
# Please commentout the rest approches and use only one approch at the time of execution. 
#Harcoded approch.
import re
example1 = 'Here is the first URL http://www.company.com' #single URL
example2= 'my link is: http://www.company.com and my another profile is https://anwartesting.html' #multiple URL

#regular expression:
#http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+

url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',example1)
print(url)
url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',example2)
print(url)

#Dynamc approch
example3 = input("Enter the text to find URL: \n")

#regular expression:
#http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+

url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',example3)
print(url)
