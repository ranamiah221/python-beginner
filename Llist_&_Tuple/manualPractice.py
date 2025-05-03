from numpy import random
# sum of the number of list..
myList=[1,3,5,6,6,7,9]
sum=0
for num in myList:
    sum +=num
print(sum)

# find greatest number in the list...
numbers=[1,2,12,3,6,9,11,7,0]
tem=0
for n in numbers:
    if(tem < n):
        tem = n 
print(tem)

x= random.randint(10)
print(x)