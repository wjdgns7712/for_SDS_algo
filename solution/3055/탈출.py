f=open('탈출.txt', 'r')
input=f.readline

R, C = map(int, input().split())
board=[list(input().rstrip()) for _ in range(R)]
dist=[[0 for _ in range(C)] for _ in range(R)]
water=[[i, j] for j in range(C) for i in range(R) if board[i][j]=='*']
start = [[i, j] for j in range(C) for i in range(R) if board[i][j]=='S'][0]

q=[[board[i][j], i, j] for i, j in water]+[['.', start[0], start[1]]]
dr=[-1, 0, 1, 0]
dc=[0, 1, 0, -1]

while q:
    t, r, c = q.pop(0)
    if board[r][c]=='D':
        print(dist[r][c])
        break
    
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<R and 0<=nc<C and board[nr][nc] not in ['X', '*']:
            if t=='*' and board[nr][nc]=='.':
                board[nr][nc]='*'
                q.append([t, nr, nc])
            elif t=='.' and board[nr][nc] in ['.', 'D'] and not dist[nr][nc]:
                dist[nr][nc]=dist[r][c]+1
                q.append([t, nr, nc])
                
else: print('KAKTUS')