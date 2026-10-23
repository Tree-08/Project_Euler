curr = 6          # 1 Dec 1900 
ans = 0
days = [3,3,0,3,2,3,2,3,3,2,3,2]

for yr in range(1901, 2001):
    for mn in range(1, 13):
        curr = (curr + days[mn-1]) % 7
        if mn == 3 and yr % 4 == 0:
            curr = (curr + 1) % 7
        if curr == 0:
            ans += 1

print(ans)