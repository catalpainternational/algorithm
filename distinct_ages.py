# Given two lists of children age, one for each class, output the list of ages that can be found in both classes.

ages_1 = [12, 13, 16, 13, 11]
ages_2 = [15, 16, 12, 15]
ages_in_both = [12, 16]


ages_1 = [5, 6, 7, 8, 9]
ages_2 = [15, 14, 13, 12, 11, 10, 9]
ages_in_both = [9]

ages_1 = [5, 6, 4]
ages_2 = [7, 8, 10]
ages_in_both = []


def find_same_age(ages_1, ages_2):
    s1 = set(ages_1)
    s2 = set(ages_2)
    return list(s1 & s2)


def mario(ages_1, ages_2):
    intersection = []
    for age in ages_1:
        if age in ages_2:
            intersection.append(age)
    return intersection
