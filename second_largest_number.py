# Write a function that takes a list of numbers, and returns the second highest number.

def second_largest_number(lista):
    # return the second highest number
    pass


second_largest_number([0, 1, 2])  # returns 1
second_largest_number([3, 2, 1])  # returns 2
second_largest_number([4, 10, 8, 9])  # returns 9
second_largest_number([32, 12, 21, 43, 0])  # returns 32

def niko(lista):
    first, second = None, None
    for n in lista:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return second

def ano(lista):
    listas = []
    max_lista = max(lista)
    for item in lista:
        if item < max_lista:
            listas.append(item)
    return max(listas)

def rapha(lista):
    max_lista = max(lista)
    max_index = lista.index(max_lista)
    lista.pop(max_index)
    return max(lista)
