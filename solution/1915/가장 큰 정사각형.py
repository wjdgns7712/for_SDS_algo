f=open('./solution/1915/input.txt', 'r')
input=f.readline

n, m = map(int, input().split())
arr, dp = [[0]*(m+1)], [[0]*(m+1)]
for i in range(n):
    inp=[0]+[1 if c=='1' else 0 for c in input().rstrip()]
    arr.append(inp)
    dp.append(inp)

def chk(r, c):
    global dp
    a = dp[r-1][c-1]
    b = dp[r][c-1]
    c = dp[r-1][c]
    return min(a, b, c)+1

answer=0
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j]:
            dp[i][j]=chk(i, j)
            answer=max(answer, dp[i][j])

print(answer*answer)

for row in dp:
    print(row)