def is_keeping_rule(place_map, x, y):
    rule_range = [
        (-2, 0), (-1, 1), (-1, 0), (-1, -1), (0, 2), (0, 1)
        , (0, -1), (0, -2), (1, 1), (1, 0), (1, -1), (2, 0)
    ]
    for d in rule_range:
        x1 = x + d[0]
        y1 = y + d[1]
        if x1 < 0 or x1 > 4 or y1 < 0 or y1 > 4:
            continue
        other_point = place_map[x1][y1]
        if other_point == "P":
            # 바로 옆에 사람이 붙어있는 경우
            if d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                return False
            # 대각선에 사람이 붙어있는 경우
            elif d == (-1, 1):
                if place_map[x - 1][y] == "X" and place_map[x][y + 1] == "X":
                    continue
                else:
                    return False
            elif d == (-1, -1):
                if place_map[x - 1][y] == "X" and place_map[x][y - 1] == "X":
                    continue
                else:
                    return False
            elif d == (1, -1):
                if place_map[x][y - 1] == "X" and place_map[x + 1][y] == "X":
                    continue
                else:
                    return False
            elif d == (1, 1):
                if place_map[x + 1][y] == "X" and place_map[x][y + 1] == "X":
                    continue
                else:
                    return False
            # 마지막으로 직선으로 두 칸 떨어진 곳에 사람 있는 경우
            elif d == (-2, 0):
                if place_map[x - 1][y] == "X":
                    continue
                else:
                    return False
            elif d == (2, 0):
                if place_map[x + 1][y] == "X":
                    continue
                else:
                    return False
            elif d == (0, 2):
                if place_map[x][y + 1] == "X":
                    continue
                else:
                    return False
            elif d == (0, -2):
                if place_map[x][y - 1] == "X":
                    continue
                else:
                    return False
    return True


def solution(places):
    answer = []

    for place in places:
        people_point = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    people_point.append((i, j))
        is_keeping = True
        for point in people_point:
            res = is_keeping_rule(place, point[0], point[1])
            if not res:
                is_keeping = False
                break

        answer.append(int(is_keeping))

    return answer