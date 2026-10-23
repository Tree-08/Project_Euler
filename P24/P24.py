N = 10
l = [i for i in range(N)]
fact = [1]*N
for i in range(1,N):
    fact[i]=fact[i-1]*i
idx = 1000000
idx-=1
ans = 0
while(len(l)):
    q = idx//fact[len(l)-1]
    idx %= fact[len(l)-1]
    ans = ans*10+l[q]
    l.remove(l[q])

print(ans)

#2783915604