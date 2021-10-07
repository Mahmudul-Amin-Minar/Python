# string = input()
# string_dict = {}

# for c in string:
#     if c in string_dict:
#         string_dict[c] += 1
#     else:
#         string_dict[c] = 1
    
# print(string_dict)

def frequency(string):
    freq = [None] * len(string)
    # print(freq)
    
    for i in range(0, len(string)):
        freq[i] = 1
        # print(freq)
        for j in range(i+1, len(string)):
            if(string[i] == string[j]):
                freq[i] = freq[i] + 1
                string = string[:j] + '0' + string[j+1:]
                # print(string)

    for i in range(0, len(freq)):
        if(string[i] != ' ' and string[i] != '0'):
            print(string[i]+str(freq[i]), end='')

frequency("ccccOddEEE")