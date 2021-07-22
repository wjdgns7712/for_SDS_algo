f=open('./solution/2243/사탕상자.txt', 'r')
input=f.readline

n = int(input())
for _ in range(n):
    cmd = input().split()
    if len(cmd)>2: # push or pop
        a, b, c = map(int, cmd)
        if c>0: #push
            pass
        else: #pop
            pass
    else: # only pop once
        a, b = map(int, cmd)
        print()
    