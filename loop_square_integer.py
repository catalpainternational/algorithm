# Write a function that takes an integer n as argument, and returns the list of the square of all integers i < n.

def f(n):
    # your code here
    for f in range (0, n):
        print (f ** 2)
        
# In the end, your function should have the following results:

f(1)# In [4]: f(1)
# Out[4]: [0]
#
f(2)# In [5]: f(2)
# Out[5]: [0, 1]
#
f(3)# In [6]: f(3)
# Out[6]: [0, 1, 4]
#
f(4)# In [7]: f(4)
# Out[7]: [0, 1, 4, 9]
#
f(5)# In [8]: f(5)
# Out[8]: [0, 1, 4, 9, 16]
