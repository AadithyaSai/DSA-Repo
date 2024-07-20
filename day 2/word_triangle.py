word = input()
n = len(word)

mid = n // 2

for i in range(n):
    print(' ' * (n-i-1), end='')

    j = mid
    for j in range(i+1):
        print(word[(mid+j)%n], end=' ')
    print()