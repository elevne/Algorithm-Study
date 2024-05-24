import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
INF = 1e9
dp = [INF] * 200001
q = deque()
q.append((n, 0))
answer = 0
if n == k:
    print(0)
    print(1)
else:
    while q:
        curr, tot = q.popleft()
        nxt = tot + 1
        if nxt <= dp[k]:
            a = curr + 1
            b = curr - 1
            c = curr * 2
            # dp 다음 것이 현재 진행경로에서 1 더한 것보다 크거나 같을 경우
            if 0 <= a <= 200000 and dp[a] >= nxt:
                # 근데 만약 그 다음이 도착 경로인 경우
                if a == k:
                    # 현제 dp 도착경로 값이 지금 경로와 동일
                    if nxt == dp[a]:
                        answer += 1
                    # 그게 더 큰 경우
                    else:
                        answer = 1
                # 그 외에는 그냥 큐에 넣기
                else:
                    q.append((a, nxt))
                dp[a] = nxt
            if 0 <= b <= 200000 and dp[b] >= nxt:
                if b == k:
                    if nxt == dp[b]:
                        answer += 1
                    else:
                        answer = 1
                else:
                    q.append((b, nxt))
                dp[b] = nxt
            if 0 <= c <= 200000 and dp[c] >= nxt:
                if c == k:
                    if nxt == dp[c]:
                        answer += 1
                    else:
                        answer = 1
                else:
                    q.append((c, nxt))
                dp[c] = nxt

    print(dp[k])
    print(answer)
