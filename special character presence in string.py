#             ANWAR SHAIKH
#             Python program set2/011
#             Title: Find Special character from string
'''This program help us to find special character is present in strin or not
============================================================
'''
# Please commentout the rest approches and use only one approch at the time of execution. 
#Firt approch.

# Example 1
import re
import time

print("Executing First example")
time.sleep(2)
str ="Welcome#anwar&here@for python\.##(okays"
spc=re.compile('[@_!#$%^&*()<>?|\/{}:]')
print("Given Data is: ",str)
time.sleep(3)


if (spc.search(str))==None:
    print("NO Special character available")
else:
    print("Special character present")
time.sleep(2)

#Example 2
print("Executing second example")
time.sleep(2)
str2="Welome Anwar for Python"
b=re.compile('[@_!#$%^&*()<>?|\/{}:]')
print("Given Data is: ",str2)
time.sleep(3)


if (b.search(str2))==None:
    print("NO Special character available")
else:
    print("Special character present")