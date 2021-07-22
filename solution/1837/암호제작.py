p, k = map(int, input().split())
primes=set([i for i in range(3, k, 2)])
if k>2: primes.add(2)
for i in range(3, int(k**0.5)+1, 2):
    primes-=set([j for j in range(i+i, k, i)])
for i in primes:
    if p%i==0:
        print('BAD', i)
        break
else: print('GOOD')