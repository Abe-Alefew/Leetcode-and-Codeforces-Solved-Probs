class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        xStrReversed = xStr[::-1]
        return xStr == xStrReversed