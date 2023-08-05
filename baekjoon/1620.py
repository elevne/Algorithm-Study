import sys
from collections import OrderedDict
input = sys.stdin.readline

n, m = map(int, input().replace("\n", "").split())
pokemons = dict()
pokemons2 = dict()
for i in range(n):
    pokemon = input().replace("\n", "")
    pokemons[pokemon] = i+1
    pokemons2[str(i+1)] = pokemon
key_set = pokemons.keys()
for _ in range(m):
    q = input().replace("\n","")
    if pokemons.__contains__(q):
        print(pokemons.get(q))
    else:
        print(pokemons2.get(q))