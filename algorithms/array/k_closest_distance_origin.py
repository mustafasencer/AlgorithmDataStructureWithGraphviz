import heapq


def solve(points, k):
    result = []

    for i in range(len(points)):
        distance = points[i][0] * points[i][0] + points[i][1] * points[i][1]
        heapq.heappush(result, (distance, points[i]))

    return [heapq.heappop(result)[-1] for _ in range(k)]


if __name__ == '__main__':
    points = [[-5, 4], [-6, -5], [4, 6]]
    k = 2
    result = solve(points, k)
    assert result == [[-5, 4], [4, 6]]
