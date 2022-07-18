#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    lix = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            lix += 1
        except IndexError:
            break
    print("")
    return (lix)
