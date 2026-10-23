N = 1000
mx = 1
num = 2

for i in range(2,N):
    s = {}
    temp = 10
    step = 0
    length = 0
    while(True):
        r = temp%i
        if(r == 0): break
        if(r in s):
            length = step - s[r]
            break
        s[r] = step
        step += 1
        temp=10*r
    
    if(length>mx):
        mx = length
        num = i
    
print(mx)
print(num)

"""
We can also firstly strip out all 2's and 5's from 'i'
then we have to find the smallest 'k' such that 10^k = 1 (mod i)
This is what we are simulating here too
so we have to efficiently calculate Euler's Totient Function
n(1-1/p1)...(1-1/pm)
"""