A = [3, 5, 4, 2]
numbers = []

for i,n in enumerate(A):
    numbers.append((n, i))
numbers.sort()

max_gap = 0
min_number = numbers[0][1]
for item in numbers:
    num = item[1]
    if num < min_number:
        min_number = num
    else:
        max_gap = max(max_gap, num - min_number)

print(max_gap)
