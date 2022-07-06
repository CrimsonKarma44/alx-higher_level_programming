#!/usr/bin/python3
def uniq_add(my_list=[]):
    listd = []
    count = 0
    for i in my_list:
       if (i in listd):
          continue
       listd.append(i)
       count += i
    return ("Result: {}".format(count))
