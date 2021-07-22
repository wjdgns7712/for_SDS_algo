f=open('./solution/1927/최소 힙.txt', 'r')
input=f.readline

# from sys import stdin
# import heapq as hq
# input=stdin.readline

# heap=[]
# for _ in range(int(input())):
#     inp=int(input())
#     if inp: hq.heappush(heap, inp)
#     else:
#         if heap: print(hq.heappop(heap))
#         else: print(0)

def push(heap, num):
    heap.append(num)
    child=len(heap)-1
    parent=child//2
    while parent and heap[parent]>heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child=parent
        parent=child//2

def pop(heap):
    if len(heap)>1:
        print(heap[1])
        heap[1]=heap[-1]
        heap.pop()
        cur=1
        while len(heap)>2:
            l, r = cur*2, cur*2+1
            min_val, min_pos = heap[l], l
            if r<len(heap) and heap[r]<min_val:
                min_val, min_pos = heap[r], r
            
            if min_val<heap[cur]:
                heap[cur], heap[min_pos] = heap[min_pos], heap[cur]
                cur=min_pos
            else: break
    else: print(0)

heap=[None]
for _ in range(int(input())):
    inp=int(input())
    if inp: push(heap, inp)
    else: pop(heap)