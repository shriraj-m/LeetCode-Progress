# two sum II

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # check left and right and add numbers till it matches target
        # if sum is too small, move left
        # if sum is too large, move right
        
        # position based
        left = 1
        right = len(numbers)

        while left < right:
            # add numbers
            total = numbers[left-1] + numbers[right-1]
            print(total)
            if total == target:
                return [left, right]
            if total < target:
                # increment left
                left += 1
            else: # total is larger than target
                right -= 1



