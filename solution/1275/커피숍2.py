f=open('./solution/1275/커피숍2.txt', 'r')
input=f.readline

# from sys import stdin
# input=stdin.readline

N, Q = map(int, input().split())
dim=1
while 2**dim<N: dim+=1
startidx, endidx = 2**dim, 2**dim+N
nums = [0 for _ in range(startidx)] + list(map(int, input().split())) + [0 for _ in range(startidx-N)]
for _ in range(dim):
    width = endidx-startidx
    for i in range(0, width+1, 2):
        nums[(startidx+i)//2] = nums[startidx+i] + nums[startidx+i+1]
    startidx//=2
    endidx//=2

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x>y: x, y = y, x
    l, r = 2**dim+x-1, 2**dim+y-1
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
    idx=2**dim+a-1
    nums[idx]=b
    while idx>1:
        nums[idx//2] = nums[idx] + (nums[idx-1] if idx%2 else nums[idx+1])
        idx//=2