f = open("names.txt",'r')
data = f.read()
data = data.split(",")
data = [i.strip('"') for i in data]
data.sort()

ans = 0

for j in range(len(data)):
    name = data[j]
    temp = 0
    for i in name:
        temp += (ord(i)-ord("A")+1)
    ans+=(temp*(j+1))

print(ans)