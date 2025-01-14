"""
Absolute distinct count
Array is sorted!
Hint: Leveraging sorted array would enable the solution to use only O(1) extra space.
"""


def solve(numbers: list[int]) -> int:
    distinct = set()
    for value in numbers:
        distinct.add(abs(value))

    return len(distinct)


def solve_v2(numbers: list[int]) -> int:
    count = len(numbers)

    i, j = 0, len(numbers) - 1

    while i < j:
        # Clear negative duplicates from the array
        while numbers[i] == numbers[i + 1]:
            count -= 1
            i += 1

        # Clear positive duplicates from the array
        while numbers[j] == numbers[j - 1]:
            count -= 1
            j -= 1

        if j == i:
            break

        _sum = numbers[i] + numbers[j]

        if _sum == 0:
            i += 1
            j -= 1
            count -= 1

        if _sum > 0:
            j -= 1
        elif _sum < 0:
            i += 1

    return count


if __name__ == "__main__":
    nums = [-5, -3, 0, 1, 3, 3]
    result = solve_v2(nums)
    assert result == 4
