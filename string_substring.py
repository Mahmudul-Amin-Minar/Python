string = 'Geeks'

for i in range(len(string)):
    for j in range(i+1, len(string)+1):
        res = string[i: j]
        print(res)