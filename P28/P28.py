N = 1001
ans = 1
for i in range(3, N+1, 2):
    temp = i*i
    ans += (4*temp - 6*(i-1))
    
print(ans)