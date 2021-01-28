"""
    Created by Mustafa Sencer Özcan on 18.05.2020.
"""


def flatten_recursive(L):
    if not L:
        return []
    elif isinstance(L[0], list):
        return flatten_recursive(L[0]) + flatten_recursive(L[1:])
    else:
        return [L[0]] + flatten_recursive(L[1:])


if __name__ == '__main__':
    L = [[2, 2, 2], [2]]
    result = flatten_recursive(L)
    print(result)
