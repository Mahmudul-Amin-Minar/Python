str1 = 'Care'
str2 = 'mina'

str1 = str1.lower()
str2 = str2.lower()

sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

if len(sorted_str1) == len(sorted_str2):
    if sorted_str1 == sorted_str2:
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")