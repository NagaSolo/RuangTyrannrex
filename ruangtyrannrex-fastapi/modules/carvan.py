# T (testcases) are between 1 to 100
# T = range(1, 100)

# first N (number of cars entering the line) are between 1 to 10_000
# second N (speed of each cars specified in first line) separated by space
# N = range(1,10_000)

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
