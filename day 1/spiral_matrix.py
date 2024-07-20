n = int(input())
arr = [list(input()) for _ in range(n)]

s = ''
rs = cs = 0
re = ce = n - 1

while rs != re:
    for i in range(cs, ce+1):
        s += arr[rs][i]
    rs += 1
    for i in range(rs, re+1):
        s += arr[i][ce]
    ce -= 1
    for i in range(ce, cs-1, -1):
        s += arr[re][i]
    re -= 1
    for i in range(re, rs-1, -1):
        s += arr[i][cs]
    cs += 1

if n % 2 == 0:
    s += arr[rs][re]

print(s)

