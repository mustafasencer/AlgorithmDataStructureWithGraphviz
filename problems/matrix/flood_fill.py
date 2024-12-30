"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
"""


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        queue = [(sr, sc, image[sr][sc])]

        while queue:
            x, y, col = queue.pop(0)
            image[x][y] = color

            if col == color:
                continue

            # check up
            if x - 1 >= 0 and image[x - 1][y] == col:
                queue.append((x - 1, y, col))

            # check down
            if x + 1 < len(image) and image[x + 1][y] == col:
                queue.append((x + 1, y, col))

            # check left
            if y - 1 >= 0 and image[x][y - 1] == col:
                queue.append((x, y - 1, col))

            # check right
            if y + 1 < len(image[0]) and image[x][y + 1] == col:
                queue.append((x, y + 1, col))

        return image


if __name__ == "__main__":
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    color = 0
    result = Solution().floodFill(image, sr, sc, color)
    print(result)
