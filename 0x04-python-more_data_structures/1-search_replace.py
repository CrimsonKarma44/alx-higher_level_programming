#!/usr/bin/python3
def search_replace(my_list, search. replace):
    listd = []
    for i in my_list:
        if i == search:
            listd.append(replace)
            continue
        listd.append(i)
    return listd
