f=open('게임.txt', 'r')
input=f.readline

from math import ceil
X, Y = map(int,input().split())
Z = Y*100//X
if Z<99: print(ceil((X*Z+X-100*Y)/(99-Z)))
else: print(-1)
