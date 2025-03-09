"""2352. Equal Row and Column Pairs"""

class Solution:                                
    def equalPairs(self, grid: List[List[int]]) -> int:

        tpse = Counter(zip(*grid))      # <-- determine the transpose
                                        #     and hash the rows

        grid = Counter(map(tuple,grid)) # <-- hash the rows of grid. (Note the tuple-map, so
                                        #     we can compare apples w/ apples in next step.)

        return  sum(tpse[t]*grid[t] for t in tpse)  # <-- compute the number of identical pairs