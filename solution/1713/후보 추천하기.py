f=open('후보 추천하기.txt', 'r')
input=f.readline

n=int(input())
rec=int(input())
order=list(map(int, input().split()))
photo=[]#cnt, time, num

time=0
for person in order:
    if not photo:
        photo.append([1, time, person])
    elif len(photo)<n and person not in list(zip(*photo))[2]:
        photo.append([1, time, person])
    elif person in list(zip(*photo))[2]:
        photo[list(zip(*photo))[2].index(person)][0]+=1
    else:
        photo.sort(key=lambda x:(x[0], x[1]), reverse=True)
        photo.pop()
        photo.append([1, time, person])
    time+=1
    
print(' '.join(list(map(str, sorted(list(zip(*photo))[2])))))