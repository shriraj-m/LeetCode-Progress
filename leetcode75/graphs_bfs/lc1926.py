"""1926. Nearest Exit from Entrance in Maze"""
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        x = entrance[0]
        y = entrance[1]
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        queue = deque([(x, y, 0)]) # step 1 starting at entrance
        # set current spot in maze to a wall, so we can only explore 1 direction
        maze[x][y] = "+"

        while queue:
            row, col, steps = queue.popleft() # perks of deque
            for dx, dy in directions: # check change in all directions
                new_row = row + dx
                new_col = col + dy
                # check if current pos is in bounds and is an empty path.
                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == ".":
                    # check if it is on either border, meaning there is a exit
                    if (new_row == 0 or new_row == m - 1) or (new_col == 0 or new_col == n - 1):
                        return steps + 1
                    # if not, then we append next area into the queue
                    maze[new_row][new_col] = "+"
                    queue.append((new_row, new_col, steps+1))
        # if all fails, then return -1 since no path
        return -1
                    