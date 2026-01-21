class TimeMap:

    def __init__(self):
        self.timemap = {} # list of [val, time]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # make sure to only create a list if the key doesnt exist
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timemap.get(key, []) # get the list of lists based on key
        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)