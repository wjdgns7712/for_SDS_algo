f=open('./solution/3955/캔디 분배.txt', 'r')
input=f.readline

# from sys import stdin
# input=stdin.readline

def gcd(a, b):
    if b>a: a, b = b, a
    while b: a, b = b, a%b
    return a

def chk(a, b):
    if gcd(a, b)!=1: return 'IMPOSSIBLE'
    if b==1: return a+1 if a<100000000 else 'IMPOSSIBLE'
    if a==1: return 1
    x0, y0, r0 = 1, 0, -a
    x1, y1, r1 = 0, 1, b
    while r1!=1:
        Q = r0//r1+1
        r0, r1 = r1, r0-r1*Q
        x0, y0, x1, y1 = x1, y1, x0 - x1*Q, y0 - y1*Q
    return y1 if y1<1000000001 else 'IMPOSSIBLE'

for _ in range(int(input())):
    print(chk(*list(map(int, input().split()))))