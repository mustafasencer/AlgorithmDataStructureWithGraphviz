"""

"""


def solution(array):
    is_circular = True
    i = 0
    while is_circular:
        if array[i] == None:
            pass


def test_(array, i):
    if array[i] == array[array[i]]:
        pass
    return test_(array[i], i)


if __name__ == "__main__":
    array = [2, 3, 1, 4, 0]
    result = solution(array)
    assert result == True
    print(result)
