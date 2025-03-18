"""216. Combination Sum III"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path):
            # check if current path is same as k
            if len(path) == k:
                # check if the sum of the path is equal to n
                if sum(path) == n and len(set(path)) == k:
                    print(f"sum of path is same as n, appending {path}")
                    combinations.append(path[:])
                    print(f"combinations = {combinations}")
                return
            
            for x in range(start,10):
                path.append(x)
                backtrack(x+1, path)
                path.pop()

        combinations = []
        backtrack(1, [])
        print(combinations)
        return combinations