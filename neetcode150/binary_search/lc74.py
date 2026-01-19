class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        top = 0
        bot = ROWS - 1

        # iterate columns first
        while top <= bot:
            row = (bot + top) // 2
            # if target is greater then last val of row, then we close towards bot
            if target > matrix[row][-1]:
                top = row + 1
            # if target is less than the first value of row, we close towards top
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # if this cant occur, then not there
        if not (top <= bot):
            return False

        # update row
        row = (bot + top) // 2
        # regular binary search now
        l = 0
        r = COLS - 1

        while l <= r: 
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False
            