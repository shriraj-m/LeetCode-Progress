"""735. Asteroid Collision"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for rock in asteroids:
            while result and rock < 0 < result[-1]: # checks rock if negative and prev pos
                if -rock > result[-1]:
                    result.pop()
                    continue
                elif -rock == result[-1]:
                    result.pop()
                break
            else:
                result.append(rock)
        return result
        