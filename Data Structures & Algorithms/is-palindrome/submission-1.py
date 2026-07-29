class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = "".join([t.lower() for t in s if t.isalnum()])
        i, j = 0, len(palindrome) - 1
        while i <= j:
            if palindrome[i] != palindrome[j]:
                return False
            i += 1
            j -= 1
        return True