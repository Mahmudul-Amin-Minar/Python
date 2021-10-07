string = input()

r_string = string[::-1]
if string == r_string:
    print('Palindrome')
else:
    print("Not Palindrome")
print(r_string)