''' Challenge: Lapindromes 

Summary:
    Finding the shortest solution to the palindrome challenges.
    Check whether string is a palindrome 

Input:
    First line of input contains a single integer T, the number of test cases.
    Each test is a single line containing a string S composed of only lowercase English alphabet.

Output:
    For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.
        
Constraints:
    1 ≤ T ≤ 100
    2 ≤ |S| ≤ 1000, where |S| denotes the length of S

'''

def palindrome(input_string):
    if input_string == reversed(input_string): 
        return 'YES'
    return 'NO'

# # using if else inside lambda
# palindrome = lambda input_string: sorted(input_string[:len(input_string)//2]) == sorted(input_string[len(input_string)//2:]) if (len(input_string)%2 == 0) else sorted(input_string[:len(input_string)//2]) == sorted(input_string[(len(input_string)//2)+1:])

# driver
if __name__ == '__main__':
    T = int(input())
    for test in range(T):
        S = input()
        print(palindrome(S))

