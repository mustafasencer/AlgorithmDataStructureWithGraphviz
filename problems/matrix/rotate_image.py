from typing import List


def rotate(matrix: List[List[int]]) -> List[List[int]]:
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix[:] = zip(*matrix[::-1])
    return matrix


def test_(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


if __name__ == "__main__":
    result = rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(result)
