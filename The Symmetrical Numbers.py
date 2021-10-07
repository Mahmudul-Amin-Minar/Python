def isPalindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (n == rev)
 
def countPal(minn: int, maxx: int):
    count = 0
    for i in range(minn, maxx + 1):
        if isPalindrome(i):
            count += 1
    return count

n = int(input())

for c in range(n):
    numbers = list(map(int, input().split()))
    x = numbers[0]
    y = numbers[1]
    if x > y:
        temp = x
        x = y
        y = temp
    print(f"Case {c+1}:", countPal(x, y))