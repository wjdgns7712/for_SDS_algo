f=open('./solution/14476/최대공약수 하나 빼기.txt', 'r')
input=f.readline

# from sys import stdin
# input=stdin.readline

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b: a, b = b, a%b
    return a

N=int(input())
LR, RL = [0 for _ in range(N)], [0 for _ in range(N)]
nums=list(map(int, input().split()))
for i in range(N):
    LR[i]=nums[i] if not i else gcd(LR[i-1], nums[i])
    RL[N-i-1]=nums[N-i-1] if not i else gcd(RL[N-i], nums[N-i-1])
maxgcd, k = LR[-1], None
for i in range(N):
    if 0<i<N-1:
        cur=gcd(LR[i-1], RL[i+1])
        if maxgcd<cur: maxgcd, k = cur, nums[i]
    elif i==0:
        if maxgcd<RL[i+1]: maxgcd, k = RL[i+1], nums[i]
    elif i==N-1:
        if maxgcd<LR[i-1]: maxgcd, k = LR[i-1], nums[i]
print(f'{maxgcd} {k}' if k else -1)