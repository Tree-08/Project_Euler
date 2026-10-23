N = 28123
d = [0]*(N+1)

for i in range(1, N//2+1):
    for j in range(2*i, N+1, i):
        d[j]+=i
        
temp = [0]*(N+1)
for i in range(1, N+1):
    if(d[i]>i):
        for j in range(1,i+1):
            if(d[j]>j and i+j<=N): temp[i+j]=1

ans = 0
for i in range(1,N+1):
    if(temp[i]==0): ans+=i
    
print(ans)