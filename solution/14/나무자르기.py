f=open('나무자르기.txt', 'r')
input=f.readline

N, M = map(int, input().split())
height=dict()
for h in map(int, input().split()):
    if h in height: height[h]+=1
    else: height[h]=1
s, e = 0, max(height.keys())
while s<=e:
    m=(s+e)//2
    if sum([(k-m)*v for k, v in height.items() if k>m])>=M:
        result=m
        s=m+1
    else: e=m-1
print(result)