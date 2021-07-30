f=open('solution/10714/input.txt', 'r')
input=f.readline

N=int(input())
dp=[[-1 for _ in range(N)] for _ in range(N)]
A=[int(input()) for _ in range(N)]
R = lambda x: (x+1)%N
L = lambda x: (x+N-1)%N

def ioi(l, r):
    if R(r)==l: return 0
    if A[L(l)]>A[R(r)]: return joi(L(l), r)
    return joi(l, R(r))

def joi(l, r):
    if R(r)==l:
        dp[l][r]=0
        return 0
    if dp[l][r]==-1: dp[l][r]=max(A[L(l)]+ioi(L(l), r), A[R(r)]+ioi(l, R(r)))
    return dp[l][r]

print(max([A[i]+ioi(i, i) for i in range(N)]))