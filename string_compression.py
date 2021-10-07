def compressed_string(string):
    compress_string = ''
    n = len(string)
    i = 0
    while i < n- 1:
        count = 1
        while (i < n - 1 and string[i] == string[i + 1]):
            count += 1
            i += 1
        i += 1

        # print(string[i - 1] + string(count), end = "")
        if count == 1:
            compress_string += (string[i - 1])
        else:    
            compress_string += (string[i - 1] + str(count))
    return list(compress_string)
 

string = ["a","a","a","b","b","a","a"]
print(compressed_string(string))
