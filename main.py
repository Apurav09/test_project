
lst = [8,14,7,1,8,8,9,3,8,3]

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count



print(countX(lst, 8))

