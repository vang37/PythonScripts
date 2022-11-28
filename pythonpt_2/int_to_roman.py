#!/usr/bin/env python3

import sys


def roman(integer):

    if (int(integer) > 3999 or int(integer) < 1):
        print("Please pick a number between 1 and 3999 (inclusive).")
        return

    matrix = [["", "M", "MM", "MMM"],
              ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
              ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
              ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]]
    string = ""
    offset = 4 - len(integer)

    for i in reversed(range(offset, 4)):
        string = matrix[i][int(integer[i - offset])] + string
    print(string)
    return string


roman(sys.argv[1])
