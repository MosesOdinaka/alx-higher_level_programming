#!/usr/bin/python3
# finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):

    list_int = list_of_integers
    if list_int == []:
        return None
    total = len(list_int)
    if total == 1:
        return list_int[0]
    elif total == 2:
        return max(list_int)
    half = int(total / 2)
    avrg = list_int[half]
    if avrg > list_int[half - 1] and avrg > list_int[half + 1]:
        return avrg
    elif avrg < list_int[half - 1]:
        return find_peak(list_int[:half])
    else:
        return find_peak(list_int[half + 1:])
