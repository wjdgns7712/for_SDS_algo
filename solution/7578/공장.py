f=open('solution/7578/input.txt', 'r')
input=f.readline

N=int(input())
dic={int(v):[i] for i, v in enumerate(input().split())}
for i, v in enumerate(input().split()):
    dic[int(v)].append(i)
dp=[[0 for _ in range(N)] for _ in range(N)]
for s, e in dic.values():
    dp[s][e]+=1
for row in dp:
    print(row)