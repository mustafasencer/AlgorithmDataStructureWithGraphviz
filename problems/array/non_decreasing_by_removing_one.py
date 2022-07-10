"""

"""


def solution(array):
    if array == sorted(array):
        return True

    for i in range(len(array)):
        remove = array[:i] + array[i + 1 :]
        if remove == sorted(remove):
            return True
    return False


if __name__ == "__main__":
    array = [1, 4, 2, 3]
    result = solution(array)
    assert result == True
    print(result)
