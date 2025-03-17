"""1466. Reorder Routes to Make All Paths Lead to the City Zero"""
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for c1, c2 in connections:
            # road from c1 to c2. 1 represents to city
            graph[c1].append((c2, 1))
            # reversed road, 0 represents from city
            graph[c2].append((c1, 0))

        print(graph)
        def dfs(node, parent):
            count = 0
            for neighbor, direction in graph[node]:
                if neighbor != parent:
                    # count edges that need to be changed
                    # add direction (0 or 1)
                    count += direction
                    # go to next node, update parent.
                    count += dfs(neighbor, node)
            return count
        
        return dfs(0, -1)
