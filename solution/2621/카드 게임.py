f=open('solution/2621/input.txt', 'r')
input=f.readline

def solve(start, end, flag):
    global card, dp
    if start==end:
        if flag==0: dp[flag][start][end]=card[start]
        else: dp[flag][start][end]=0
        return dp[flag][start][end]
    
    if dp[flag][start][end]: return dp[flag][start][end]
    
    if flag==0: dp[flag][start][end] = max(solve(start+1, end, 1)+card[start], solve(start, end-1, 1)+card[end])
    else: dp[flag][start][end] = min(solve(start+1, end, 0), solve(start, end-1, 0))

    return dp[flag][start][end]

T = int(input())
for _ in range(T):
    N=int(input())
    card = list(map(int, input().split()))
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(2)]
    print(solve(0, N-1, 0))