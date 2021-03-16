#             ANWAR SHAIKH
#             Python program set2/003
#             Title: Factorial Number
'''This programe will help to get factorial number.
Logic/Concept: lets say i have num =5
so we need to multiply all the number before num.
e.g num=5 
1 * 2 * 3 * 4 * 5= 120
============================================================
'''
# Please commentout the rest approches and use only one approch at the time of execution. 
#approch 1
num=20
factorial=1
if num<0:
    print("factorial does not exits for negative Numbers")
elif num==0:
    print("The factorial of 0 is :1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of", num, "is:",factorial)


#approch 2 recursive function.
def facto(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * facto(n-1) #5 *4*3*2*1

num2= 5
print("Factorial of ",num2, "is: ", facto(num2))

