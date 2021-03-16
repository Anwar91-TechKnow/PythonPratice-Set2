#             ANWAR SHAIKH
#             Python program set2/009
#             Title: Swap first and last elemenents
'''This program help us to swap first and last elements from given data
This have total 5 approches
============================================================
'''
# Please commentout the rest approches and use only one approch at the time of execution. 
mylist= [2,45,23,13,90]
size=len(mylist)
print(mylist)

#First Approch using temperory variable approch
temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp

print("List after swapping : ",mylist)

#Second approch
mylist[0],mylist[size-1]= mylist[size-1],mylist[0]

print("List after swapping with second approch : ",mylist)

#Third Approch Tuple
get=(mylist[0],mylist[size-1]) # packed
mylist[size-1],mylist[0]= get #unpacked.
print("List after swapping with Third approch : ",mylist)

#Fourth Approch: *Operand
start,*middle,end=mylist
print(start)
print(end)
print(middle)

mylist=[end,*middle,start]
print("List after swapping with Fouth approch : ",mylist)

#Fifth Apporch: pop ()
first=mylist.pop(0) #2
last =mylist.pop(-1) #90

mylist.insert(0, last)
mylist.append(first)

print("List after swapping with Fifth approch : ",mylist)