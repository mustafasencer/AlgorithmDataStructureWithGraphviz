def rotate(matrix: list[list[int]]) -> list[list[int]]:
    """Do not return anything, modify matrix in-place instead."""
    matrix[:] = zip(*matrix[::-1], strict=False)
    return matrix


def test_(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


if __name__ == "__main__":
    result = rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
