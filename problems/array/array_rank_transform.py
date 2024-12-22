from typing import List


def array_rank_transform(arr: List[int]) -> List[int]:
    """
    1.
    """
    copy_ = arr.copy()
    copy_.sort()
    store = {}
    counter = 1
    for i in copy_:
        if i not in store:
            store[i] = counter
            counter += 1

    for i in range(len(arr)):
        arr[i] = store[arr[i]]

    return arr


def array_rank_transform_2(arr):
    """
    1.
    """
    store = {val: index + 1 for index, val in enumerate(sorted(set(arr)))}

    for i in range(len(arr)):
        arr[i] = store[arr[i]]

    return arr


if __name__ == "__main__":
    result = array_rank_transform([40, 10, 20, 30])
    _result = array_rank_transform_2([40, 10, 20, 30])
    assert result == _result
    print(result)
