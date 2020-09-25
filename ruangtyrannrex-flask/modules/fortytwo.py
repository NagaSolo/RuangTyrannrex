# iterate over list

# if reach index[42] stop

# display previous elements

# res = [i for i in fortytwo if i is not fortytwo[42] else break]
# print(res)

"""Variable list answer"""
# fortytwo = [1, 2, 88, 42, 99]
# for el in fortytwo:
#     if el is not 42:
#         print(el)
#     else:
#         break

"""With standard input answer"""
while True:
    notfortytwo = int(input())
    if notfortytwo is not 42:
        print(notfortytwo)
    else:
        break