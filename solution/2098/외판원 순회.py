f=open('solution/2098/input.txt', 'r')
input=f.readline

INF=50000000
N=int(input())
cost=[map(int, input().split()) for _ in range(N)]
cost=[[n if n else INF for n in cost[i]] for i in range(N)]
dp=[[INF for _ in range(1<<N)] for _ in range(N)]

def tsp(id, visited):
    if visited==(1<<N)-1: return cost[id][0]
    if dp[id][visited]!=INF: return dp[id][visited]
    for i in range(N):
        if visited & 1<<i: continue
        if cost[id][i]==INF: continue
        nxt = visited | 1<<i
        dp[id][visited] = min(dp[id][visited], tsp(i, nxt)+cost[id][i])
    return dp[id][visited]
print(tsp(0, 1))