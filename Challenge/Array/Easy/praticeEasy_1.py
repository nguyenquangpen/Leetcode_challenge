class Solution_1920(object):
    def buildArray(self, nums):
        result = [nums[nums[i]] for i in range(len(nums))]
        return result

class Solution_1929(object):
    def getConcatenation(self, nums):
        return nums + nums

class Solution_2011(object):
    def finalValueAfterOperations(self, operations):
        result = 0
        for i in operations:
            if i == "++X" or i == "X++":
                result += 1
            else:
                result -= 1
        return result

class Solution_3190(object):
    def minimumOperations(self, nums):
        operations = 0
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                operations += 1
            elif remainder == 2:
                operations += 1

        return operations

class Solution_1470(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result

class Solution_2942(object):
    def findWordsContaining(self, words, x):
        result, cnt = [], 0
        for i in words:
            if x in i:
                result.append(cnt)
            cnt += 1
        return result

class Solution_1672(object):
    def maximumWealth(self, accounts):
        result = float('-inf')
        for i in accounts:
            result = max(sum(i), result)
        return result

class Solution_1863(object):
    def subsetXORSum(self, nums):
        return (reduce(lambda x, y: x | y, nums)) << (len(nums) - 1)


class Solution_2373(object):
    def largestLocal(self, grid):
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                # Find the maximum value in the 3x3 submatrix
                maxVal = max(
                    grid[i][j], grid[i][j + 1], grid[i][j + 2],
                    grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                    grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]
                )
                maxLocal[i][j] = maxVal
        return maxLocal


if __name__ == '__main__':
   pass

