# First input the total number of people
# convert it into binary form and add first digit to last
# print the decimal value of newly created binary value


def josephus(n):
    binary_value = list(bin(n))
    binary_value += binary_value[2]
    binary_value[2] = '0'
    survived = int("".join(binary_value), 2)

    return survived

n = int(input("How many people " ))
print(josephus(n))
