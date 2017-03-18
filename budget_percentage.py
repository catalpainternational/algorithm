import random

# [12, 12]
# total = 12 + 12 = 24
# 12/24 * 100 = 0.5 * 100 = 50
# [50, 50]
#
# [3, 7]
# total = 10
# 3/10 * 100 = 30
# 7/10 * 100 = 70
# [30, 70]

def budget_percentages(budgets):
    percentages = []
    total = sum(budgets)
    for budget in budgets:
        percentages.append(budget/total * 100)
    return percentages

    total = sum(budgets)
    return [budget/total * 100 for budget in budgets]

def ano(budgets):
    total = sum(budgets)
    return [budget/total * 100 for budget in budgets]

budget_percentages([15, 5, 30])  # return [30, 10, 60]
budget_percentages([12, 12])  # return [50, 50]
budget_percentages([3])  # return [100]

budget_percentages([random.randint(0, 100) for i in range(10)])
