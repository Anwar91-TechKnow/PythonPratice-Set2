#             ANWAR SHAIKH
#             Python program set2/006
#             Title: Palindrome string/numbers
'''This programe will help to get to know whether provided string or digits are 
palindrome or not.
Logic/Concept: Palindrome means after reversing string both are same reveresed and original then
it is palindrome string.
Some examples of palindromic words are redivider, deified, civic, radar,
level, rotor, kayak, reviver, racecar, madam, and refer. , 91019,91219
============================================================
'''

a=input("Enter the string value: ")
b=a [:: -1] #here i am reversing given string

#Validating whether reverse string and original string are same or not.
if a==b:
    print("This is the palindrome")
else:
    print("This is not palindrome")
