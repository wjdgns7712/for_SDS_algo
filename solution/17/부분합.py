f=open('부분합.txt', 'r')
input=f.readline

N, S = map(int, input().split())
nums=list(map(int, input().split()))

l, r, length = 0, 0, N+1
total=nums[0]
while r<N:
    if total<S:
        r+=1
        if r<N: total+=nums[r]
    elif total>=S:
        length=min(r-l+1, length)
        total-=nums[l]
        l+=1
        if l>r:
            r+=1
            if r<N: total+=nums[r]
print(length if length<N+1 else 0)