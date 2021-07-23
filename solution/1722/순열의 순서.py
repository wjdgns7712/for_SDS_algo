f=open('./solution/1722/input.txt', 'r')
input = f.readline

from math import factorial as F
N=int(input())
inp=list(map(int, input().split()))
t, arr = inp[0], inp[1:]
numset=list(range(1, N+1))
if t==1:
    idx=arr[0]
    arr=[]
    for i in range(N-1):
        fact=F(N-1-i)
        target=(idx-1)//fact
        idx-=target*fact
        arr.append(numset[target])
        numset.remove(numset[target])
    arr.append(numset.pop())
    print(*arr)
else:
    idx=1
    for i, n in enumerate(arr[:-1]):
        idx+=numset.index(n)*F(N-1-i)
        numset.remove(n)
    print(idx)