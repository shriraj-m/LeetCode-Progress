"""547. Number of Provinces"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # initialize a visited set()
        visited = set()
        # depth first search from current city
        def dfs(current_city):
            if current_city in visited:
                return
            
            visited.add(current_city)
            # we want to loop through an enumerated version of is connected's current cities.
            # this will make the next_city variable a counter
            # if is_connected and next_city are not in visited, we can move forward
            for next_city, if_connected in enumerate(isConnected[current_city]):
                print(f"{next_city} | {if_connected}")
                if if_connected and next_city not in visited:
                    dfs(next_city)

        provinces = 0
        for city in range(len(isConnected)):
            print(f"city: {city}")
            if city not in visited:
                dfs(city)
                provinces += 1
        
        return provinces
            