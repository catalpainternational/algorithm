# Write a function that takes a list of numbers, and returns the second highest number.

def f(lista):
    # return the second highest number
    frt, scd = None, None
    for n in lista:
        if n > frt:
            frt, scd = n, frt
        elif frt > n > scd:
            scd = n
    return scd


f([0, 1, 2])  # returns 1
f([3, 2, 1])  # returns 2
f([4, 10, 8, 9])  # returns 9
f([32, 12, 21, 43, 0])  # returns 32
