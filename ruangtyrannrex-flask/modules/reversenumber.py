
""" Reverse the number given

    Accept the number(int) input
    Reverse the given number
"""

# # given list of number method
# normal_number = [5, 4, 3, 2, 1]
# normal_number.reverse()
# print(normal_number)

"""
Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.


Output
For each test case, display the reverse of the given number N, in a new line.
"""

# standard input method
# Accepted solution
test = int(input())
for i in range(test):
    number_input = int(input())
    splitted_list = list(str(number_input))
    splitted_list.reverse()
    combined_string = ''.join(splitted_list)
    combined_number = int(combined_string)
    print(combined_number)