import sys
input = sys.stdin.readline

word = input().replace("\n", "")
cnt = {}
for i in range(26):
    cnt[i] = 0
length = len(word)
for i in range(length):
    cnt[ord(word[i]) - 97] += 1
result = []
for v in cnt.items():
    result.append(str(v[1]))
print(" ".join(result))
