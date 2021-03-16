#             ANWAR SHAIKH
#             Python program set2/005
#             Title: Maximum and minimum 
'''This programe will help to get minimum and maximum number from given data
Logic/Concept: a []={1,20,50,100}
so here max will be 100
and minimum will be 1
============================================================
'''
# Please commentout the rest approches and use only one approch at the time of execution. 
#1. finding max element
a=[120,5,12,69,100,2]
#here we are assuming first element is max value.

max=a[0]
n=len(a)

for i in range(1,n):
    if a[i]>max:
        max=a[i]
        
print("Maximum is :",max)

#2. Findig minimum element
b=[20,5,12,69,100,2]

min=b[0]
n2=len(b)
for i in range(1,n):
    if a[i]<min:
        min=a[i]
        
print("minimum is :", min)

