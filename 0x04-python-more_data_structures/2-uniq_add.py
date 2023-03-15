#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    summ = 0
    for num in my_list:
        if num not in new:
            new.append(num)
            summ += num
    return summ
