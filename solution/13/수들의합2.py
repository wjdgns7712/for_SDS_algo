f=open('수들의합2.txt', 'r')
input=f.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

total, l, r, cnt = A[0], 0, 0, 0
while r<N:
    if total<M:
        r+=1
        if r<N: total+=A[r]
    elif total>M:
        total-=A[l]
        l+=1
    else:
        cnt+=1
        total-=A[l]
        l+=1
        r+=1
        if r<N: total+=A[r]
print(cnt)