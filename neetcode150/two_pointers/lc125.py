class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non-alphanumeric characters
        clear_text = ''.join(char for char in s if char.isalnum())
        # convert everything to lower case
        clear_text = clear_text.lower()

        # iterate over the text, carrying one pointer at the start and one at the end
        # pos
        start = 0 
        end = len(clear_text)-1

        while start < end:
            # compare letters
            if clear_text[start] != clear_text[end]:
                return False
            else: # mean they are the same
                start += 1
                end -= 1
            
        return True