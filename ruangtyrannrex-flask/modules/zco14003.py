'''Challenge: ZCO14003: Zonal Computing Olympiad 2014, 30 Nov 2013

Summary:
    You are developing a smartphone app. You have a list of potential customers for your app. Each customer has a budget and will buy the app at your declared price if and only if the price is less than or equal to the customer's budget.


    You want to fix a price so that the revenue you earn from the app is maximized. Find this maximum possible revenue.


    For instance, suppose you have 4 potential customers and their budgets are 30, 20, 53 and 14. In this case, the maximum revenue you can get is 60 .


Input format:
    Line 1 : N, the total number of potential customers.

    Lines 2 to N+1: Each line has the budget of a potential customer.

Output format:
    The output consists of a single integer, the maximum possible revenue you can earn from selling your app.


Sample Input 1
    4
    30
    20
    53
    14

Sample Output 1
    60

Sample Input 2
    5
    40
    3
    65
    33
    21

Sample Output 2
    99

Test data:
    Each customers' budget is between 1 and 108, inclusive.


    Subtask 1 (30 marks) : 1 ≤ N ≤ 5000.

    Subtask 2 (70 marks) : 1 ≤ N ≤ 5×105.

Live evaluation data:
    There are 15 test inputs on the server during the exam. The grouping into subtasks is as follows.

    • Subtask 1: Test inputs 0,…,5

    • Subtask 2: Test inputs 6,…,14

Note:
    The answer might not fit in a variable of type int. 
    We recommend that you use variables of type long long to read the input and compute the answer. 
    If you use printf and scanf, you can use %lld for long long.

Pseudocode:
    - More than 1 customer -> etc customer1, customer2, customer3, .. customerN
    - Each has their own budget -> customer1_budget, customer2_budget, customer3_budget, .. customerN_budget
    - if declared_price <= customer_budget then buy, else not buy
    - declared_price must be price that brings the most revenue
    - greedy approach algorithm to set declared_price

'''

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
