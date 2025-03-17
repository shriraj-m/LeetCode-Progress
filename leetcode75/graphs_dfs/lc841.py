"""841. Keys and Rooms"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(current_room):
            if current_room in visited:
                return
            
            visited.add(current_room) # add current room to set

            for key in rooms[current_room]:
                dfs(key)
            
        dfs(0) # we start at 0
        len_of_visit = len(visited)
        return len_of_visit == len(rooms)
