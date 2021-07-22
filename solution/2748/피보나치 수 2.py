n=int(input())
a, b, c = 0, 1, 1
for _ in range(n-1):
    c=a+b
    a, b = b, c
print(c)