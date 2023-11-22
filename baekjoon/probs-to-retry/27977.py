import sys
import bisect

input = sys.stdin.readline

L, N, K = map(int, input().split())
charge_stations = list(map(int, input().split()))

minimum_capacity = (L // (K+1))
if L % (K+1) != 0:
    minimum_capacity += 1

charge_stations.append(L)
station_distance = [(charge_stations[0], 0, 1)] + [(charge_stations[i+1] - charge_stations[i], i+1, i+2) for i in range(N)]
station_distance.sort(key=lambda x:x[0])

bisect.insort_left(station_distance, (3, 0, 2))
print(station_distance)