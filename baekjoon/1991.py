import sys

input = sys.stdin.readline
N = int(input())

tree = dict()

for _ in range(N):
    n, l, r = input().split()
    tree[n] = (l, r)

def nlr(node):
    print(node, end="")
    l, r = tree.get(node)
    if l != ".":
        nlr(l)
    if r != ".":
        nlr(r)

def lnr(node):
    l, r = tree.get(node)
    if l != ".":
        lnr(l)
    print(node, end="")
    if r != ".":
        lnr(r)

def lrn(node):
    l, r = tree.get(node)
    if l != ".":
        lrn(l)
    if r != ".":
        lrn(r)
    print(node, end="")

nlr("A")
print()
lnr("A")
print()
lrn("A")