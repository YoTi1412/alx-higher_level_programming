#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    uniq_list = []
    add = 0
    for num in my_list:
        if num not in uniq_list:
            add += num
            uniq_list.append(num)
    return add