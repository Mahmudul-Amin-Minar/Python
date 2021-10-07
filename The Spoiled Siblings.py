n = int(input())

for _ in range(n):
    t = int(input())
    sum = t*(t+1)//2
    sum2 = 0
    i=1
    while i <= t:
        sum2 += i
        i = 2*i
    print((sum - sum2) - sum2)