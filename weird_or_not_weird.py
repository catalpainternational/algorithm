# https://www.hackerrank.com/challenges/py-if-else

def f(n):
    if n % 2 == 1:
        print('Weird')
    # equivalent: elif n in range(2, 5):
    elif 2 <= n and n <= 5:
        print('Not Weird')
    # equivalent: elif n in range(6, 21):
    elif 6 <= n and n <= 20:
        print('Weird')
    elif n > 20:
        print('Not weird')

f(1)  # should print Weird
f(2)  # should print Not weird
f(3)  # should print Weird
f(8)  # should print Weird
f(20)  # should print Weird
f(21)  # should print Weird
