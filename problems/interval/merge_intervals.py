from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if result and result[-1][-1] >= interval[0]:
                result[-1][-1] = max(interval[-1], result[-1][-1])
            else:
                result.append(interval)
        return result


if __name__ == "__main__":
    result = Solution().merge([[1, 4], [2, 3]])
    print(result)
