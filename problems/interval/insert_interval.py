def solution(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    intervals.append(newInterval)
    result = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if result and result[-1][-1] >= i[0]:
            result[-1] = max(result[-1][-1], i[-1])
        else:
            result.append(i)
    return result


if __name__ == "__main__":
    result = solution([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
