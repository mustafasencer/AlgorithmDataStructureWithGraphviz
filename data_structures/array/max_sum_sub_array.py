def max_sum_sub_array(array):
    max_so_far = 0
    max_ending_here = 0

    for elem in array:
        max_ending_here = max_ending_here + elem
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far


def test(array):
    max_current = 0
    max_so_far = 0

    for elem in array:
        max_current = max_current + elem
        if max_current < 0:
            max_current = 0
        if max_so_far < max_current:
            max_so_far = max_current
    return max_so_far


if __name__ == '__main__':
    array = [-1, 3, -5, 2, 4, 1, -3, 6, -2, 4, 2]
    result = max_sum_sub_array(array)
    print(result)
