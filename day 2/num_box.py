n = int(input())

start = 0
end = 2*n-1
for i in range(2*n-1):
    val = n + 1
    for j in range(2*n-1):
        if j <= start:
            val -= 1
        if j >= end:
            val += 1
        print(val, end=' ')
    start += 1
    end -= 1
    print()

