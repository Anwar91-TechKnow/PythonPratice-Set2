#             ANWAR SHAIKH
#             Python program set2/002
#             Title: Prime Number
'''This is python progaramm where i am checking whether provided number is prime or not.
concept/logic: Prime number is the number which is greather than 1 and it should have two factor
1. Number should devided by 1
2. Number should devided by itself.
============================================================
'''
num =int(input("Please enter the number: "))
count=0

if num>1:
    for i in range(1, num+1):
        if(num%i)==0:
            count=count+1
    if count==2:
        print("This is prime number")
    else:
        print("This is Not prime number")
