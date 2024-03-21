import sys

input = sys.stdin.readline

N, M = map(int, input().split())
know_the_truth = [False] * (N+1) # 1번 인덱스부터 시작

second_line = list(map(int, input().split()))
if len(second_line) > 1:
    for idx in second_line[1:]:
        know_the_truth[idx] = True

party_member_graph = [[False] * (N+1) for _ in range(N+1)]
parties = []
party_truth_stack = []
for _ in range(M):
    party_members = list(map(int, input().split()))[1:]
    parties.append(party_members)
    for i in range(len(party_members)):
        for j in range(i+1, len(party_members)):
            party_member_graph[party_members[i]][party_members[j]] = True
            party_member_graph[party_members[j]][party_members[i]] = True
for idx, knows in enumerate(know_the_truth):
    if knows:
        for i, t in enumerate(party_member_graph[idx]):
            if t:
                party_truth_stack.append(i)

while party_truth_stack:
    mem = party_truth_stack.pop()
    know_the_truth[mem] = True
    for other, con in enumerate(party_member_graph[mem]):
        if con and not know_the_truth[other]:
            party_truth_stack.append(other)

result = 0
for party in parties:
    can_lie = True
    for mem in party:
        if know_the_truth[mem]:
            can_lie = False
    if can_lie:
        result += 1
print(result)