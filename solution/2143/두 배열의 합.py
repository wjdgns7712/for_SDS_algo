T=int(input())
n=int(input())
A=list(map(int, input().split()))
m=int(input())
B=list(map(int, input().split()))

asum=sorted([sum(A[i:j]) for i in range(n) for j in range(i+1, n+1)])
bsum=sorted([sum(B[i:j]) for i in range(m) for j in range(i+1, m+1)], reverse=True)

cnt=0
ai, bi = 0, 0
n, m = len(asum), len(bsum)
while ai<n and bi<m:
    if asum[ai]+bsum[bi]>T: bi+=1
    elif asum[ai]+bsum[bi]<T: ai+=1
    else:
        a, b = 1, 1
        while ai<n-1 and asum[ai]==asum[ai+1]:
            a+=1
            ai+=1
        ai+=1
        while bi<m-1 and bsum[bi]==bsum[bi+1]:
            b+=1
            bi+=1
        bi+=1
        cnt+=a*b
print(cnt)
