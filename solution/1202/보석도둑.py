f=open('./solution/1202/보석도둑.txt', 'r')
input=f.readline

# from sys import stdin
import heapq as hq
# input=stdin.readline

N, K = map(int, input().split())
bosuks=sorted([list(map(int, input().split())) for _ in range(N)], reverse=True)
bags=sorted([int(input()) for _ in range(K)])
tmp, price = [], 0
for bag in bags:
    while bosuks and bosuks[-1][0]<=bag: hq.heappush(tmp, -bosuks.pop()[1])
    if tmp: price-=hq.heappop(tmp)
print(price)