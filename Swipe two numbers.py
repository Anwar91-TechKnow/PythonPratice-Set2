#             ANWAR SHAIKH
#             Python program set2/001
#             Title: Swipe two Numbers
'''This is python progaramm where i am doing swapping of two number using two approches.
1. with hardcorded values
2. Values taken from user
also in this i have added how to use temporary variable as well as without delcaring 
temporary varibale.
============================================================
'''
# Please commentout the rest approches and use only one approch at the time of execution. 
import time
#1. with hardcorded values
num1=55
num2=30

print("Value of num1 before swapping : ",num1)
print("Value of num2 before swapping : ",num2)
time.sleep(2)

#now here created temporary varibale to store value of numbers.
a = num1 #it will store value in variable called a
num1=num2 #here num2 will replace with num1 value
num2=a #here num2 value swapped with num1 which 

#swapping is done
print("Value of num1 After swapping : ",num1)
print("Value of num2 after swapping : ",num2)
time.sleep(3)

#second example:
#2. Values taken from user
#we can take input from user also
num_one=input("Enter first number : ")
num_two=input("Enter Second number : ")
time.sleep(3)

b = num_one 
num_one=num_two 
num_two=b
print("Value of first number After swapping : ",num_one)
print("Value of second number swapping : ",num_two)
time.sleep(3)
#without delcaring temporary variable.
num1=20
num2=5

print("Value of num1 before swapping : ",num1)
print("Value of num2 before swapping : ",num2)
time.sleep(3)
num1,num2=num2,num1

#swapping is done
print("Value of num1 After swapping : ",num1)
print("Value of num2 after swapping : ",num2)
time.sleep(3)