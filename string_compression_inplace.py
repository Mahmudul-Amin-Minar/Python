def compress(chars) -> int:
    compress_string = ''
    n = len(chars)
    i = 0
    while i < n- 1:
        count = 1
        while (i < n - 1 and chars[i] == chars[i + 1]):
            count += 1
            i += 1
        i += 1

        # print(string[i - 1] + string(count), end = "")
        if count == 1:
            # compress_string += (chars[i - 1])
            # chars[count-i] = str(count)
            pass
        else:    
            # compress_string += (chars[i - 1] + str(count))
            chars[count-i-2] = str(count)
    # chars = list(compress_string)
    print(chars)
    return len(chars)

compress(["a","a","b","b","c","c","c"])