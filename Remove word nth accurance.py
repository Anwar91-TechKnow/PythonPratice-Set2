#             ANWAR SHAIKH
#             Python program set2/010
#             Title: Remove Word NTH accuance.
'''This program help us remove word which appered second time.
============================================================
'''
# Please commentout the rest approches and use only one approch at the time of execution. 
#Firt approch
arr = ['Shaikh', 'Shaikh', 'of', 'best', 'Anwar']
print(arr)
inp = input('Enter value: ')
count = 0

for i in arr:
    if i == inp:
      count += 1
      if count == 2:
         arr.remove(i)
print(arr)

#Second Approch
mylist=['Greeks','best','you','Greeks']
word='Greeks'
n=2
print("Original List : ",mylist)
count=0

for i in range(0,len(mylist)):
    if (mylist[i])==word:
        count=count+1
    if count==n:
        del mylist[i]

print("Updated list: ", mylist)
