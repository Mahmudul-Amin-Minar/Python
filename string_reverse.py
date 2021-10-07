def string_reversing(string):
    l = len(string) - 1
    reversed_string = ''
    
    while(l>=0):
        reversed_string += string[l]
        l -= 1

    print(reversed_string)

string_reversing("Hello World!")

def string_reversing_default(string):
    reversed_string = string[::-1]
    print(reversed_string)

string_reversing_default("Hello World!")


def string_reverse_by_word(string):
    split_string = string.split(' ')
    s = ' '.join(split_string[::-1])
    print(s)

string_reverse_by_word("Hello World")