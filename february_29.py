# Write a function that takes a year number, and returns the number of days in February.

def ano(n):
    if n/4.0 == n/4:
        return 29
    else:
        return 28

def ony(n):
    if n % 4 == 0:
        return 29
    else:
        return 28

def niko_and_mario(n):
    if n in range(0, n+1, 4):
        return 29
    else:
        return 28

# f(2017) returns 28
# f(2016) return 29
# f(2020) return 29

# To time the function in ipython:
# %timeit for x in range(1900, 2100): niko_and_mario(x)
