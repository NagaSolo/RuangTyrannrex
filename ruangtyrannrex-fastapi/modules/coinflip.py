'''Brainstorming
    T -> number of testcases, range(1,10)
        integer G -> at first line of each T, range(1, 2000)
            I N Q -> at the first line of each G
    integer I(initial state of coins, 1(guess number of heads at the end) or 2(guess number of tails at the end)) 
    integer N(number of coins and rounds), range(1, 10^9)
    integer Q(1(guess number of heads at the end) or 2(guess number of tails at the end))
'''

def flip_coin(I, N, Q):
    ''' coin will be alternating after each round example T H T H T H'''
    if (int(N)%2 == 0 or I == Q):
        print(int(int(N)/2))
    else:
        print(int(((int(N)-1)/2)+1))

T = int(input())
if T>=1 and T<=10:
    for test in range(T):
        G = int(input())
        if G>=1 and G<=2_000:
            for game in range(G):
                I, N, Q = input().strip().split()
                if (int(I) == 1 or int(I) == 2) and (int(Q) == 1 or int(Q) == 2):
                    if int(N)>=1 and int(N)<=10_000_000_000:
                        flip_coin(I, N, Q)
                    else:
                        exit()
                else:
                    exit()
        else:
            exit()
else:
    exit()