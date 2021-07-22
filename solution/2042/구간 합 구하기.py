f=open('./solution/2042/구간 합 구하기.txt', 'r')
input=f.readline

# from sys import stdin
# input=stdin.readline

N, M, K = map(int, input().split())
dim=1
while 2**dim<N: dim+=1
startidx, endidx = 2**dim, 2**dim+N
nums=[int(input()) if startidx<=i<endidx else 0 for i in range(2**(dim+1))]
for _ in range(dim):
    width = endidx-startidx
    for i in range(0, width+1, 2):
        nums[(startidx+i)//2] = nums[startidx+i] + nums[startidx+i+1]
    startidx//=2
    endidx//=2

for _ in range(M+K):
    t, a, b = map(int, input().split())
    if t==1:
        idx=2**dim+a-1
        nums[idx]=b
        while idx>1:
            nums[idx//2] = nums[idx] + (nums[idx-1] if idx%2 else nums[idx+1])
            idx//=2
    else:
        l, r = 2**dim+a-1, 2**dim+b-1
        total=0
        while l<=r:
            if l%2:
                total+=nums[l]
                l=(l+1)//2
            else: l//=2
            if r%2: r//=2
            else:
                total+=nums[r]
                r=(r-1)//2
        print(total)