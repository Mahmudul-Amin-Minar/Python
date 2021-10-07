# [a-z] = 97-122
# [A-Z] = 65-90

string = input()

swapped_string = ''

for c in string:
    if ord(c) >= 97 and ord(c) <= 122:
        swapped_string += chr(ord(c) - 32)
    elif ord(c) >= 65 and ord(c) <= 90:
        swapped_string += chr(ord(c) + 32)
    else:
        swapped_string += c

print(swapped_string)