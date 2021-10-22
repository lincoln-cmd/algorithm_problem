class Solution:
    def isPalindrome(self, x: int) -> bool:
        if list(str(x)) == list(reversed(list(str(x)))):
            return True
        else:
            return False
