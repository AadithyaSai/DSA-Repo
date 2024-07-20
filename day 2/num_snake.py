m, n = [int(x) for x in input().split()]

right = True
digits = len(str(m))

for i in range(m//n + 1):
    if right:
        for j in range(i*n + 1, min((i+1)*n + 1, m)):
            print(f"%{digits}d"%j, end=' ')
    else:
        for j in range((i+1)*n, i*n, -1):
            if j > m:
                print(f"%{digits}s"%" ", end=' ')
            else:
                print(f"%{digits}d"%j, end=' ')
            
    print()
    right = not right
    