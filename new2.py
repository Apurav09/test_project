#count unique values inside a list

l1 = []
lst = [8,14,7,1,8,8,9,3,8,3,6]


count = 0
for ele in lst:
    if ele not in l1:
        count += 1
        l1.append(ele)


print(count)