''' Challenge CARVAN

Overview:
    - repo: github.com/NagaSolo/0703_tyrannrex_4-CARVAN
    - July 3rd, 2020 craft
    - count maximum number of cars in a race with maximum speed at straight line

Summary:
    - One segment of the circuit in a race was a long straight road. 
    - It was impossible for a car to overtake other cars on this segment.
    - Therefore, a car had to lower down its speed if there was a slower car in front of it.
    - How many cars were moving at their maximum speed.

    - Formally, 
        you're given the maximum speed of N cars in the order they entered the long straight segment of the circuit.
    - Each car prefers to move at its maximum speed.
    - If that's not possible because of the front car being slow, 
        it might have to lower its speed.
    - It still moves at the fastest possible speed while avoiding any collisions.
    - For the purpose of this problem, you can assume that the straight segment is infinitely long.

    - Count the number of cars which were moving at their maximum speed on the straight segment.

Input:
    - The first line of the input contains a single integer T denoting the number of test cases to follow.
    - Description of each test case contains 2 lines.
    - The first of these lines contain a single integer N, the number of cars.
    - The second line contains N space separated integers, 
        denoting the maximum speed of the cars in the order they entered the long straight segment.

Output:
    - For each test case, 
    output a single line containing the number of cars which were moving at their maximum speed on the segment.

Example:
    ##### Sample Input:
    3
    1
    10
    3
    8 3 6
    5
    4 5 1 2 3

    ##### Sample Output:
    1
    2
    2

    ##### Constraints
    1 ≤ T ≤ 100
    1 ≤ N ≤ 10,000
    All speeds are distinct positive integers that fit in a 32 bit signed integer.
    Each input file will not be larger than 4 MB (4,000,000,000 bytes) in size.

    ##### WARNING! The input files are very large. Use faster I/O.

Pseudocode:
    # T (testcases) are between 1 to 100
    # T = range(1, 100)

    # first N (number of cars entering the line) are between 1 to 10_000
    # second N (speed of each cars specified in first line) separated by space
    # N = range(1,10_000)

'''

def test_validitor(test):
    # T = range(1, 100)
    if test >= 1 & test <=100:
        return test
    else:
        exit()

def cars_counter_validitor(numbers):
    # N = range(1, 10_000)
    if int(numbers) >= 1 & int(numbers) <= 10_000:
        return numbers
    else:
        exit()

def cars_w_maximum_speed(cars_speed_list):
    car_counter = 1
    for indeks in range(len(cars_speed_list) - 1):
        if len(cars_speed_list) == 1:
            print(len(cars_speed_list))
        elif len(cars_speed_list) == 0:
            car_counter -= 1
            print(car_counter)
        elif cars_speed_list[indeks + 1] <= cars_speed_list[indeks]:
            car_counter += 1
    print(car_counter)


test = int(input())
for t in range(test):
    numbers = int(input())
    cars_counter_validitor(numbers)
    cars_speed_list = [i for i in input().split()]
    if len(cars_speed_list) != numbers:
        break
    else:
        cars_w_maximum_speed(cars_speed_list)
