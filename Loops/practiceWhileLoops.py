# print numbers from 1 to 100.

i= 1
while i <=100:
    print(i)
    i +=1

# print numbers from 100 to 1.

i= 100
while i >=1:
    print(i)
    i -=1

# print the multiplication table of a number n.

x = int(input("Enter the table number :"))
i=1
while i <=10:
    print (x * i)
    i+= 1


# print the elements of the follwing list using a loop.
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

nums= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1

#heros list print.
heros =["rana", "roni", "emtiaz", "mishal"]
idx= 0 
while idx < len(heros):
    print(heros[idx])
    idx +=1

# search for a number x in this tuple using loop.
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums =(1, 4, 9,16, 25, 36, 49, 64, 81, 100)
searchNumber = 36
i=0
while i < len(nums):
    if (nums[i] == searchNumber):
        print("Found at idx: ",i)
    i+= 1


