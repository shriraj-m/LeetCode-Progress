"""VALID SUDOKU"""
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create sets of everything
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                # skip when there is a dot
                if board[r][c] == ".":
                    continue
                # now check if its in the set
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False # it was in the set

                # now add value to the sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
