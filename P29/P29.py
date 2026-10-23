def binpow(a,b):
    if(b==0): return 1
    temp = binpow(a,b//2)
    temp *= temp
    if(b&1): temp*=a
    return temp

N = 100
s = set()
for a in range(2, N+1):
    for b in range(2, N+1):
        s.add(binpow(a,b))

print(len(s))