''' good chance to make use of python generator

T -> testcases
d[0] -> first element
d[1] -> second element
d[k-1] -> last element
K -> len(d[k-1])

input (if T=1):
T
K d[0] d[1]

output (if T=1):
YES or NO

'''

def generate_luhn(dn, d0, d1):
    num_list = [d0, d1]
    while len(num_list) < dn:
        num_list.append(sum(num_list))
    return num_list

# driver
if __name__ == "__main__":
    test = [[5, 3, 4], [13, 8, 1], [760399384224, 5, 1]]
    for t in test:
        print(generate_luhn(t[0], t[1], t[2]))