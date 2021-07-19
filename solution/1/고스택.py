f=open('고스택.txt', 'r')
input=f.readline

# from sys import stdin
# input=stdin.readline

cmddict={'NUM':0, 'POP':1, 'INV':2, 'DUP':3, 'SWP':4, 'ADD':5, 'SUB':6, 'MUL':7, 'DIV':8, 'MOD':9}

inp=input().rstrip()
while inp[0]!='Q':
    cmds=[]
    while inp[0]!='E':
        if len(inp)>3:
            cmd, num = inp.split()
            cmd, num = cmddict[cmd], int(num)
        else: cmd, num = cmddict[inp], None
        cmds.append([cmd, num])
        inp=input().rstrip()
    n=int(input())
    for _ in range(n):
        stack=[int(input())]
        for cmd, num in cmds:
            try:
                if cmd==1: stack.pop()
                elif cmd==2: stack[-1]*=-1
                elif cmd==3: stack.append(stack[-1])
                elif cmd==4: stack[-1], stack[-2] = stack[-2], stack[-1]
                elif cmd>4:
                    a, b = stack.pop(), stack.pop()
                    if cmd==5: stack.append(a+b)
                    elif cmd==6: stack.append(b-a)
                    elif cmd==7: stack.append(a*b)
                    elif cmd==8:
                        if (a<0 and b<0) or (a>0 and b>0): stack.append(abs(b)//abs(a))
                        else: stack.append(-(abs(b)//abs(a)))
                    elif cmd==9:
                        if b<0: stack.append(-abs(b%a))
                        else: stack.append(abs(b%a))
                elif cmd==0: stack.append(num)
            except:
                print('ERROR')
                break
        else:
            if not stack: print('ERROR')
            elif len(stack)>1 or abs(stack[-1])>1000000000: print('ERROR')
            else: print(stack[-1])
    inp=input().rstrip()
    if not inp: inp=input().rstrip()
    if inp[0]!='Q':print()