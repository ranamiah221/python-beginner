# write a recursive function to calculate the sum of first n natural numbers.

def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n
total=cal_sum(5)
print(total)

# write a recursive function to print all elements in a list .
# hint: use list & index as parameters.

heros=['ironman','superman','thor','spiderman']
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

print_list(heros)