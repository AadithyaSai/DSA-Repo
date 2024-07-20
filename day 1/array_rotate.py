#input

n = int(input())
arr = [int(x) for x in input().split()]
d, r = input().split()
r = int(r)

# operation

# Space Efficient
# if d == 'r':
#     for _ in range(r):
#         tmp = arr[-1]
#         for i in range(n-2, -1, -1):
#             arr[i+1] = arr[i]
#         arr[0] = tmp
# else:
#     for _ in range(r):
#         tmp = arr[0]
#         for i in range(1, n):
#             arr[i-1] = arr[i]
#         arr[-1] = tmp

# Time Efficient
tmp = [0 for _ in range(n)]
if d == 'r':
    for i in range(n):
        tmp[(i+r)%n] = arr[i]
else:
    for i in range(n):
        tmp[(i-r)%n] = arr[i]
arr = tmp

# output
print(arr)