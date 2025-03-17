"""994. Rotting Oranges"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # m x n
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        all_minute = 0
        # find the 2s in grid
        
        rotten = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    rotten.append([row,col])

        for x,y in rotten:
            queue.append((x,y,0)) # send x,y and minute 0
        
        while queue:
            # grab location of rotten orange
            cr, cc, minute = queue.popleft()
            all_minute = minute
            # check the 4 directions
            for dx, dy in directions:
                nr = cr + dx # new row = cur row + dx
                nc = cc + dy # new col = cur col + dy
                # only work if its in bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # check if new pos is a fresh orange
                    if grid[nr][nc] == 1:
                        print(f"fresh orange - ({nr},{nc})")
                        # make it rotten, push position into queue
                        grid[nr][nc] = 2
                        queue.append((nr,nc,minute+1))
        # set of grid
        grid_set = set(orange for row in grid for orange in row)
        if 1 not in grid_set:
            return all_minute
        else:
            return -1
            





