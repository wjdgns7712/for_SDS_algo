f=open('가르침.txt', 'r')
input=f.readline

from itertools import combinations as combi

n, k = map(int, input().split())
if k>4:
    char={'a','n','t','i','c'}
    words=[set(input().rstrip()[4:-4])-char for _ in range(n)]
    print(words)
    k-=5
    pp_words=[]
    answer=0
    for combo in combi(set(map(''.join, words)), k):
        cnt=sum([1 for need in words if not(need-set(combo))])
        answer=max(cnt, answer)
        if answer==n: break
    print(answer)
else: print(0)