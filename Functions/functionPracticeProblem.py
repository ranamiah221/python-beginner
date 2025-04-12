# waf to print the length of a list.(list is the parameter).

cities=['dhaka','tangail','khulna','rajshahi','barishal','savar']
def print_len(list):
    print(len(list))
print_len(cities)

# waf to print the elements of a list in a single line.(list is the parameter).

heros=['ironman','thor','superman','spiderman']
def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(heros)

# waf to find the factorial of n. (n is the parameter).

n = int(input("Enter the factorial num : "))
def fact(value):
    fac=1
    for i in range(1, value + 1):
        fac = fac * i
    print(fac)
fact(n)

# waf to convert USD to INR.

def converter(usd_value):
    inr_value = usd_value * 83
    print(usd_value, "USD =", inr_value, "INR")
converter(100)

# odd even check using function

def checkNumber(number):
    if(number % 2 ==0):
        print("Even")
    else:
        print('Odd')
checkNumber(1)