"""
    Created by Mustafa Sencer Özcan on 23.05.2020.
"""
from typing import List

"""Backtracking / DFS """


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board, word, i, j):
                    result = True
        return result

    def backtrack(self, board, word, i, j) -> bool:
        if not word:
            return True
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or word[0] != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        result = self.backtrack(board, word[1:], i - 1, j) \
                 or self.backtrack(board, word[1:], i, j - 1) \
                 or self.backtrack(board, word[1:], i + 1, j) \
                 or self.backtrack(board, word[1:], i, j + 1)
        board[i][j] = temp
        return result


if __name__ == '__main__':
    result = Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'ABCB')
    print(result)
