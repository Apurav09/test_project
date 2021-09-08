#count occurence of an element with list comprehension
lst = [8,14,7,1,8,8,9,3,8,3]


list =  [ele for ele in lst if ele == 8]

count = len(list)

print(count)

