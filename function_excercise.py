my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 18, 20,
           22123142, 21214124213, 132213431, 123, 213, 31234, ]


def highest_even(list):
    new_list = []
    for item in list:
        if item % 2 == 0:
            new_list.append(item)
        else:
            pass
    return max(new_list)


print(highest_even(my_list))
