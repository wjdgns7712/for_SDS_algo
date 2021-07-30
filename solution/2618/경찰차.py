f=open('solution/2618/input.txt', 'r')
input=f.readline

N=int(input())
W=int(input())
E= [[]] + [list(map(int, input().split())) for _ in range(W)]
dp = [[0 for _ in range(W+1)] for _ in range(W+1)]

def dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def solve(a, b):
    if a==W or b==W: return 0
    if dp[a][b]: return dp[a][b]
    
    nxt = max(a, b)+1
    distA = dist([1, 1], E[nxt]) if a==0 else dist(E[a], E[nxt])
    distB = dist([N, N], E[nxt]) if b==0 else dist(E[b], E[nxt])
    
    dp[a][b] = min(distA+solve(nxt, b), distB+solve(a, nxt))
    return dp[a][b]

def path(a, b):
    if a==W or b==W: return 0
    
    nxt = max(a, b)+1
    distA = dist([1, 1], E[nxt]) if a==0 else dist(E[a], E[nxt])
    distB = dist([N, N], E[nxt]) if b==0 else dist(E[b], E[nxt])
    
    if dp[nxt][b]+distA < dp[a][nxt]+distB:
        print(1)
        path(nxt, b)
    else:
        print(2)
        path(a, nxt)

print(solve(0, 0))
path(0, 0)