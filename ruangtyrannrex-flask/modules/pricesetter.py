
# More than 1 customer -> etc customer1, customer2, customer3, .. customerN
# Each has their own budget -> customer1_budget, customer2_budget, customer3_budget, .. customerN_budget
# if declared_price <= customer_budget then buy, else not buy
# declared_price must be price that brings the most revenue
# greedy approach algorithm to set declared_price

# backtracking method
def get_max_profit_from_budget(list_of_sorted_budget):
    number_of_budget = len(list_of_sorted_budget)
    list_of_each_max_profit = []
    for budget in list_of_sorted_budget:
        max_profit_each_budget = budget*number_of_budget
        number_of_budget -= 1
        list_of_each_max_profit.append(max_profit_each_budget)
    print(max(list_of_each_max_profit))

N = int(input())
customer_budget_list = []
for customer_budget in range(N):
    customer_budget_list.append(int(input()))

customer_budget_list.sort() # sort list inplace

get_max_profit_from_budget(customer_budget_list)

# # pseudo case for minimum value
# print(min(customer_budget_list)*len(customer_budget_list))

# # pseudo case for maximum value
# print(max(customer_budget_list))

# pseudo case for in between value
"""
    a = [n, n+1, n+2, n+3 ... n+n]
    min = a[n]
    max = a[n+n]
    if a[n+1] == min; a[n+1]*len(a)
    if a[n+1] != min; a[n+1]*(len(a)-n) 

"""
