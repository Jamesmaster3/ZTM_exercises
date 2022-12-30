# create one line lambda expreassion that creates squared ist

my_list = [5, 4, 3]

print(list(map(lambda item: item ** 2, my_list)))

# sort a list based on second value in tuple

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(a[1][1])

a.sort(key=lambda item: item[1])
print(a)
