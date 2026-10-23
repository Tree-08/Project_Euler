"""
n^2 + an + b

b -> prime
1+a+b -> prime
4+2a+b -> prime
9+3a+b

b atleast 41
=> a is odd too
"""
N = 2000000
prime = [1]*N
prime[0]=prime[1]=0

for i in range(2, int(N**0.5)+1):
    if(prime[i]):
        for j in range(2*i, N, i):
            prime[j]=0

mx = 39
ma = 1
mb = 41
M = 1000
for a in range(-M+1, M+1, 2):
    for b in range(41, M+1, 2):
        if(prime[b]==0): continue
        f = lambda x: x**2+a*x+b
        for x in range(1000):
            if(f(x)<=1 or prime[f(x)]==0):
                if(x-1>mx):
                    mx=x-1
                    ma=a
                    mb=b
                break

print(mx)
print(ma)
print(mb)
print(ma*mb)