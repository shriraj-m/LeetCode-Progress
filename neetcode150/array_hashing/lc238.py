"""PRODUCT OF ARRAY EXCEPT SELF"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for num in nums:
            if num:
                product *= num
            else:
                print("add zero count")
                zero_count += 1

        # if there are two or more zeros, we know that every answer will be 0
        # if there is only 1, then everything will be 0 except pos 0
        answer = []
        for num in nums:
            if zero_count >= 2:
                answer.append(0)
            elif zero_count == 1:
                if num == 0:
                    answer.append(product)
                else:
                    answer.append(0)
            else:
                answer.append(int((product / num)))
        
        print(answer)
        return(answer)
        
