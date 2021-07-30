f=open('solution/7579/input.txt', 'r')
input=f.readline

N, M = map(int, input().split())
mems = map(int, input().split())
cost = map(int, input().split())

now_m, now_c = 0, 0
for c, m in sorted(zip(cost, mems), key=lambda x:(x[0], -x[1])):
    if now_m<M:
        now_c+=c
        now_m+=m
    else: break
print(now_c)