def max_summed_sub_array(array):
    for i in range(1, len(array)):
        if array[i - 1] > 0:
            array[i] += array[i - 1]
    return max(array)


def _test(array):
    for i in range(1, len(array)):
        if array[i - 1] > 0:
            array[i] = array[i - 1] + array[i]
    return max(array)


if __name__ == '__main__':
    array = [1, 3, -5, 5]
    result = _test(array)
    print(result)
