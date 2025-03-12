"""649. Dota2 Senate"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        for idx in range(len(senate)):
            if senate[idx] == "R":
                radiant.append(idx)
            else:
                dire.append(idx)

        track = len(senate)
        while len(radiant) and len(dire):
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(track)
            else:
                dire.append(track)
            track += 1

        if len(radiant):
            return "Radiant"
        else:
            return "Dire"
