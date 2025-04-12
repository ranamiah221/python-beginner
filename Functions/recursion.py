# print 1 to 50 using recursive function...
def show(n):
    if(n==51):
        return
    print(n)
    show(n+1)
show(1)
# print 1 to 50 using loop
i=1
while i <=50:
    print(i)
    i +=1