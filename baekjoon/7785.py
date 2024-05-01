import sys
input = sys.stdin.readline

n = int(input())
people = dict()
for _ in range(n):
    name, op = input().split()
    if op == "enter":
        people[name] = True
    else:
        people[name] = False
p = list(people.items())
p.sort(key=lambda x:x[0], reverse=True)
for n, b in p:
    if b:
        print(n)