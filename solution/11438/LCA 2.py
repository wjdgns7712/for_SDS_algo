f=open('./solution/11438/input.txt', 'r')
input=f.readline        

depth=[]
parent=[[]]
nodes={}
N, K = 0, 0

def main():
    global depth, nodes, parent, N, K
    
    N=int(input())
    K=0
    while 2**K<=N: K+=1
    depth = [0 for _ in range(N+1)]
    parent = [[0 for _ in range(K)] for _ in range(N+1)]
    nodes={i:[] for i in range(1, N+1)}
    for _ in range(N-1):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    dfs(1, 1)
    fill()
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(lca(a, b))

def dfs(id, cnt):
    global depth, nodes
    depth[id]=cnt
    for nxt in nodes[id]:
        if depth[nxt]==0:
            dfs(nxt, cnt+1)
            parent[nxt][0]=id

def fill():
    global N, K, parent
    for j in range(1, K):
        for i in range(1, N+1):
            parent[i][j]=parent[parent[i][j-1]][j-1]

def lca(a, b):
    global depth, parent, N, K
    
    if depth[a]<depth[b]: a, b = b, a
    
    for i in range(K-1, -1, -1):
        if 2**i <= depth[a]-depth[b]: a=parent[a][i]        
    if a==b: return a
    
    for i in range(K-1, -1, -1):
        if parent[a][i]!=parent[b][i]:
            a=parent[a][i]
            b=parent[b][i]
    
    return parent[a][0]
            
if __name__=="__main__":
    main()