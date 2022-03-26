def solve(arr, target, current):
    if len(arr) == current + 1:
        return -1
    if arr[current] == target:
        return current
    return solve(arr, target, current + 1)


if __name__ == '__main__':
    arr = [9, 8, 1, 8, 1, 7]
    target = 1
    current = 0
    result = solve(arr, target, current)
    assert result == 2
