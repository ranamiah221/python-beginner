# print the elements of the following list using a loop.
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in nums:
    print(num)

# search for a number x in this tuple using loop.
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49

for n in tup:
    if (n == x):
        print("Found")
        break
else:
    print("Not found")
