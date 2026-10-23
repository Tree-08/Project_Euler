N = 10000
l = [0,1]
curr = 1
while(N):
    l.append(l[-1]+l[-2])
    if(len(str(l[-1]))!=curr):
        if(curr+1==1000):
            print(len(l)-1)
            break
        curr = len(str(l[-1]))
    N-=1