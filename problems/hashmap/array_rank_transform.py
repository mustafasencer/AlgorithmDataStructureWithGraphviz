def array_rank_transform(arr: list[int]) -> list[int]:
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


def array_rank_transform_v2(arr):
    store = {val: index + 1 for index, val in enumerate(sorted(set(arr)))}
    return [store[item] for item in arr]


if __name__ == "__main__":
    result = array_rank_transform([40, 10, 20, 30])
    result_v2 = array_rank_transform_v2([40, 10, 20, 30])
    assert result == result_v2
