# WAP to check if a number entered by the user is odd or even.
number=int(input("Enter a integer number: "))
if(number % 2 == 0):
    print("Even")
else:
    print("Odd")
# WAP to find the greatest of 3 numbers enterd by the user.
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))

if(num1 >= num2 and num1 >= num3):
    print("Greatest number is :", num1)
elif(num2 >= num1 and num2 >= num3):
    print("Greatest number is :", num2)
else:
    print("Greatest number is :", num3)

# WAP to check if a number is a multiple of 7 or not.

saven= int(input("enter number: "))
if(saven % 7 == 0):
    print("Multiple of 7")
else:
    print("not a multiple")

# WAP to find the greatest of 4 numbers enterd by the user.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter four number: "))

if(a >= b and a>=c and a>=d):
    print("A is a greatest number: ", a)
elif(b >= c and b >= d):
    print("B is a greatest number: ", b)
elif(c >= b and c >= d):
    print("C is a greatest number: ", c)
else:
    print("D is a greatest number: ", d)