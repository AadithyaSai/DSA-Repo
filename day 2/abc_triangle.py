n = int(input())

for i in range(n):
    print('  ' * (n-i-1), end='')

    ascii = ord('a')
    for j in range(2*i+1):
        print(chr(ascii), end=' ')

        if j >= i:
            ascii -= 1
        else:
            ascii += 1
    print()