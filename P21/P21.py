N = 10000
d = [0]*(N+1)

for i in range(1, N//2+1):
    for j in range(2*i, N+1, i):
        d[j]+=i

ans = []
for i in range(1,N+1):
    if(d[i]<=N and d[d[i]] == i and d[i]!=i):
        ans.append(i)
    
# print(d[d[220]])

print(sum(ans))