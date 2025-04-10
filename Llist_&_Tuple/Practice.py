# WAP to ask the user to enter names of their 3 favorite moives & store them in a list.

# moives =[]
# moives.append(input("Enter your first moive name: "))
# moives.append(input("Enter your second moive name: "))
# moives.append(input("Enter your third moive name: "))

# print(moives)

# wap to check if a list contains a palindrome of elements.
list= [1,2,3,2,1]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("Palindrome")
else:
    print("Not Palindrome")

