'''1431. Kids With the Greatest Number of Candies'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        most_candy = max(candies)

        for kid in range(len(candies)):
            if candies[kid] + extraCandies >= most_candy:
                result.append(True)
            else:
                result.append(False)
        return result