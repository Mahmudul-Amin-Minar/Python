# 5 row 4 column
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 17 18 19 20

rc = input().split()
r, c = int(rc[0]), int(rc[1])
# print(r, c)

array_2d = []

for _ in range(r):
    array = list(map(int, input().split()))
    array_2d.append(array)

print(array_2d)