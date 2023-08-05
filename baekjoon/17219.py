import sys
input = sys.stdin.readline

n, m = map(int, input().split())
passwords = dict()
for _ in range(n):
    site, pwd = input().split()
    passwords[site] = pwd
for _ in range(m):
    s = input().replace("\n","")
    print(passwords.get(s))