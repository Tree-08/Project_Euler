
import math

with open("words.txt", "r") as f:
    data = f.read()

words = data.split(",")
ans = 0

def chk(word_sm):
    temp = 8 * word_sm + 1
    r = math.isqrt(temp)
    return r * r == temp

for word in words:
    word = word.strip().lower()
    word_sm = 0

    for ch in word:
        if 'a' <= ch <= 'z':
            word_sm += ord(ch) - ord('a') + 1

    if chk(word_sm):
        ans += 1

print(ans)
