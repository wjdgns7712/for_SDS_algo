f = open('./solution/5719/input.txt', 'r')
input = f.readline

# from sys import stdin
from heapq import heappop, heappush
# input = stdin.readline

MAX = float('inf')

class Node:
    def __init__(self):
        self.dist = MAX;
        self.parent = []
        self.adj = {}
            
def dijkstra(N, nodes, S):
    for i in range(N):
        nodes[i].dist = MAX if i != S else 0
    
    hq = [(0, S)]
    visit = [False for _ in range(N)]
    while hq:
        _, cur = heappop(hq)
        visit[cur] = True
        for to, cost in nodes[cur].adj.items():
            if not visit[to]:
                if nodes[to].dist > nodes[cur].dist + cost:
                    nodes[to].dist = nodes[cur].dist + cost
                    nodes[to].parent = [cur]
                elif nodes[to].dist == nodes[cur].dist + cost:
                    nodes[to].parent.append(cur)
                heappush(hq, (cost, to))

def remove(target, S, nodes):
    if target!=S:
        for p in nodes[target].parent:
            del nodes[p].adj[target]
            remove(p, S, nodes)
    
N, M = map(int, input().split())
while N!=0 and M!=0:
    nodes = [Node() for _ in range(N)]
    S, D = map(int, input().split())
    for _ in range(M):
        u, v, p = map(int, input().split())
        nodes[u].adj[v]=p
    
    dijkstra(N, nodes, S)
    remove(D, S, nodes)
    dijkstra(N, nodes, S)
    
    print(nodes[D].dist if nodes[D].dist!=MAX else -1)
    N, M = map(int, input().split())