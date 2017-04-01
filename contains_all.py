# You are given a list, and a list of lists
# return whether the list contains all the other lists

big_list = [1, 2, 3, 4, 5, 10, 7]
smaller_lists = [
    [2, 3],
    [4, 5],
    [1, 10]
]
# should return True

big_list = [4, 5, 6, 2, 4]
smaller_lists = [
    [4, 5, 6],
    [2, 3],
    [6, 2]
]
# should return False

big_list = [4, 5, 2]
smaller_lists = [
    [4, 5],
    [2, 2, 2, 4, 5],
    [1]
]
# should return False


def contains_smaller_lists(big_list, smaller_lists):
    # should return a boolean
    pass
