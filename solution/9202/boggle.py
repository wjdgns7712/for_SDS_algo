f=open('./solution/9202/boggle.txt', 'r')
input=f.readline

# from sys import stdin
# input=stdin.readline

class node():
    hit=False
    end=False
    def __init__(self):
        self.hit=False
        self.end=False
        self.child=[None for _ in range(26)]
        
    def clear(self):
        self.hit=False
        for i in range(len(self.child)):
            if self.child[i]: self.child[i].clear()
    
    def haschild(self, c):
        return self.child[ord(c)-ord('A')]!=None
    
    def getchild(self, c):
        return self.child[ord(c)-ord('A')]


def containsNode(word):
    global root
    cur = root
    for c in word:
        idx=ord(c)-ord('A')
        if not cur.child[idx]: return False
        cur=cur.child[idx]
    return True

root = node()

def insert(word):
    global root
    cur = root
    for c in word:
        idx=ord(c)-ord('A')
        if not cur.child[idx]: cur.child[idx]=node()
        cur=cur.child[idx]
    cur.end=True

for _ in range(int(input())):
    insert(input().rstrip())
input()

visited=[[False for _ in range(4)] for _ in range(4)]
dx=[0, 1, 1, 1, 0, -1, -1, -1]
dy=[-1, -1, 0, 1, 1, 1, 0, -1]

def search(x, y, word, node):
    visited[y][x]=True
    if not node.hit and node.end:
        node.hit=True
        strset.add(word)
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if (0<=nx<4 and 0<=ny<4) and not visited[ny][nx] and node.haschild(board[ny][nx]):
            search(nx, ny, word+board[ny][nx], node.getchild(board[ny][nx]))
    visited[y][x]=False

scoredic={1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5, 8:11}
for _ in range(int(input())):
    strset=set()
    board = [input().rstrip() for _ in range(4)]
    for y in range(4):
        for x in range(4):
            if root.haschild(board[y][x]): search(x, y, board[y][x], root.getchild(board[y][x]))
    # [search(x, y, board[y][x], root.getchild(board[y][x])) for x in range(4) for y in range(4) if root.haschild(board[y][x])]
        
    score, word, count = 0, 'Z', 0
    for item in strset:
        score+=scoredic[len(item)]
        count+=1
        if len(word)<=len(item): word=sorted([item, word])[0]
    print(score, word, count)
    root.clear()
    input()