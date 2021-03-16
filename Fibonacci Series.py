#             ANWAR SHAIKH
#             Python program set2/004
#             Title: Fibonacci Series
'''This programe will help to get Fibonacci Series.
Logic/Concept: Fibonacci Series means is the total of two presiding numbers.
e.g = 0 1  1 2 3 5 8 13
============================================================
'''

n1=0
n2=1

print(n1)
print(n2)

for i in range(2,10):
    sum=n1+n2  
    print(sum) 
    n1=n2
    n2=sum

